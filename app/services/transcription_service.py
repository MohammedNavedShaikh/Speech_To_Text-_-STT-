# app\services\transcription_service.py
from flask import jsonify
from logger import get_logger
from app.model import load_whisper_model

logger = get_logger(__name__)

def transcribe_audio(file_path):
    try:
        model = load_whisper_model()
        result = model.transcribe(file_path)

        detected_language = result.get("language")
        if detected_language not in ["en", "hi"]:
            logger.error(f"Unsupported language detected: {detected_language}")
            raise jsonify({"error": "Unsupported language detected. Only English and Hindi are allowed."})

        logger.info(f"Transcription successful for language: {detected_language}")
        return result["text"]

    except RuntimeError as e:
        logger.error(f"Runtime error during transcription: {str(e)}")
        raise jsonify({"error": str(e)})
    except Exception as e:
        logger.error(f"An unexpected error occurred during transcription: {str(e)}")
        raise jsonify({"error": "An unexpected error occurred during transcription."})
