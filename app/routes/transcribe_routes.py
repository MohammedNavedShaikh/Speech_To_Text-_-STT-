import os
from flask import Blueprint, request, jsonify, render_template
from app.services.transcription_service import transcribe_audio
from app.services.refinement_service import refine_text
from app.model import initialize_llm
from logger import get_logger

logger = get_logger(__name__)

transcribe_bp = Blueprint('transcribe', __name__)
UPLOAD_FOLDER = "uploads"

@transcribe_bp.route('/transcribe', methods=['POST'])
def transcribe():
    """Handle audio file transcription."""
    if 'audio' not in request.files:
        logger.error("No audio file part in the request.")
        return jsonify({"error": "No audio file uploaded"}), 400

    audio_file = request.files['audio']
    audio_file_path = os.path.join(UPLOAD_FOLDER, "temp_audio.wav")

    try:
        audio_file.save(audio_file_path)
        logger.info("Audio file saved successfully.")

        transcription = transcribe_audio(audio_file_path)
        logger.info("Transcription successful.")

        llm = initialize_llm()
        refined_text = refine_text(transcription, llm)
        logger.info("Text refinement successful.")

        return render_template("result.html", transcription=transcription, refined_text=refined_text)

    except Exception as e:
        logger.error(f"Error processing audio file: {e}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    finally:
        if os.path.exists(audio_file_path):
            os.remove(audio_file_path)
            logger.info("Temporary audio file removed.")
