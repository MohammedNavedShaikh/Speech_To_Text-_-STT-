import os
from flask import Blueprint, request, jsonify, render_template
from app.services.transcription_service import transcribe_audio
from app.services.refinement_service import refine_text
from app.model import initialize_llm
from logger import get_logger

logger = get_logger(__name__)
upload_bp = Blueprint('upload', __name__)

UPLOAD_FOLDER = "uploads"

@upload_bp.route("/upload", methods=["POST"])
def upload_audio():
    if 'file' not in request.files:
        logger.error("No file part in the request.")
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    if file.filename == '':
        logger.error("No selected file.")
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    try:
        file.save(filepath)
        logger.info(f"File {file.filename} uploaded successfully.")

        transcription = transcribe_audio(filepath)
        llm = initialize_llm()
        refined_text = refine_text(transcription, llm)

        return render_template("result.html", transcription=transcription, refined_text=refined_text)

    except Exception as e:
        logger.error(f"Error processing file {file.filename}: {e}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    finally:
        if os.path.exists(filepath):
            os.remove(filepath)
            logger.info(f"Temporary file {file.filename} removed.")
