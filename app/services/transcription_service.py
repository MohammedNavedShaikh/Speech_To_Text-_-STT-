from deep_translator import GoogleTranslator # type: ignore
from app.services.logger_service import LoggerService
from app.model import WhisperModelLoader

logger = LoggerService.get_logger(__name__)

class TranscriptionService:
    @staticmethod
    def transcribe_audio(file_path):
        try:
            if not isinstance(file_path, str) or not file_path.strip():
                logger.error("Invalid file path provided.")
                raise ValueError("File path must be a non-empty string.")
            
            logger.info(f"Starting transcription for file: {file_path}")
            
            whisper_loader = WhisperModelLoader()
            model = whisper_loader.load_model()

            result = model.transcribe(file_path)
            if not result or "language" not in result or "text" not in result:
                logger.error("Transcription result is incomplete or invalid.")
                raise RuntimeError("Transcription failed. Result does not contain required data.")

            detected_language = result.get("language")
            logger.info(f"Detected language: {detected_language}")

            allowed_languages = ["en", "hi"]
            if detected_language not in allowed_languages:
                logger.error(f"Unsupported language detected: {detected_language}")
                raise ValueError(
                    f"Unsupported language detected. Allowed languages are: {', '.join(allowed_languages)}."
                )

            if detected_language == "hi":
                logger.info("Detected Hindi language. Translating to Hindi (if needed).")
                translated_text = GoogleTranslator(source="auto", target="hi").translate(result["text"])
                if not translated_text.strip():
                    logger.error("Translation failed: No valid text returned.")
                    raise RuntimeError("Translation to Hindi failed. Received empty result.")
                result["text"] = translated_text
                logger.info("Translation to Hindi completed successfully.")

            logger.info("Transcription completed successfully.")
            return result

        except ValueError as ve:
            logger.error(f"ValueError: {ve}")
            raise ValueError(f"Error: Invalid input - {ve}")

        except RuntimeError as re:
            logger.error(f"RuntimeError during transcription: {str(re)}")
            raise RuntimeError(f"Transcription failed - {re}")

        except Exception as e:
            logger.error(f"An unexpected error occurred: {str(e)}")
            raise RuntimeError(f"An unexpected error occurred during transcription: {e}")

        finally:
            logger.info(f"Transcription process completed (success or failure).")