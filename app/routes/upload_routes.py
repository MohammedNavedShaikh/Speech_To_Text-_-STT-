import os
import uuid
import mimetypes
from retrying import retry  # type: ignore
from werkzeug.utils import secure_filename  # type: ignore
from flask import Blueprint, request, render_template  # type: ignore
from app.services.logger_service import LoggerService
from app.services.refinement_service import RefinementService
from app.services.transcription_service import TranscriptionService

logger = LoggerService.get_logger(__name__)
upload_bp = Blueprint('upload', __name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_MIME_TYPES = {"audio/mpeg", "audio/wav", "audio/x-wav", "audio/x-m4a", "audio/mp3"}

@retry(wait_exponential_multiplier=1000, stop_max_attempt_number=5)
def transcribe_with_retry(service, filepath):
    return service.transcribe_audio(filepath)

@retry(wait_exponential_multiplier=1000, stop_max_attempt_number=5)
def refine_with_retry(service, transcription):
    return service.refine_text(transcription)

@upload_bp.route("/upload", methods=["POST"])
def upload_audio():
    error_message = None
    filepath = None
    unique_filename = None

    try:
        if 'file' not in request.files:
            error_message = "No file uploaded."
            logger.error(error_message)
            return render_template("index.html", error_message=error_message), 400

        file = request.files['file']

        if file.filename.strip() == '':
            error_message = "No file selected."
            logger.error(error_message)
            return render_template("index.html", error_message=error_message), 400

        original_filename = secure_filename(file.filename)
        file_extension = os.path.splitext(original_filename)[1]
        unique_filename = f"{uuid.uuid4().hex}{file_extension}"
        filepath = os.path.join(UPLOAD_FOLDER, unique_filename)

        mime_type, _ = mimetypes.guess_type(original_filename)
        if mime_type not in ALLOWED_MIME_TYPES:
            error_message = "File format not supported. Please upload a valid audio file."
            logger.error(f"Unsupported file format: {mime_type} for file '{original_filename}'.")
            return render_template("index.html", error_message=error_message), 400

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        file.save(filepath)
        logger.info(f"File '{unique_filename}' uploaded successfully to '{UPLOAD_FOLDER}'.")

        transcription_service = TranscriptionService()
        transcription = transcribe_with_retry(transcription_service, filepath)

        refinement_service = RefinementService()
        refined_text = refine_with_retry(refinement_service, transcription)

        return render_template(
            "result.html",
            transcription=transcription["text"],
            refined_text=refined_text
        )

    except ValueError as ve:
        error_message = f"Input error: {str(ve)}"
        logger.error(error_message)
        return render_template("index.html", error_message=error_message), 400

    except RuntimeError as re:
        error_message = f"Processing error: {str(re)}"
        logger.error(error_message)
        return render_template("index.html", error_message=error_message), 500

    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        logger.error(error_message)
        return render_template("index.html", error_message=error_message), 500

    finally:
        if filepath and os.path.exists(filepath):
            os.remove(filepath)
            logger.info(f"Temporary file '{unique_filename}' removed.")
