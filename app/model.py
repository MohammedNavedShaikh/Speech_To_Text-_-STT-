import whisper  # type: ignore
from config import ConfigManager
from langchain_groq import ChatGroq  # type: ignore
from app.services.logger_service import LoggerService

logger = LoggerService.get_logger(__name__)


class LLMInitializer:
    def __init__(self, api_key: str = None, model_name: str = None):
        self.api_key = api_key or ConfigManager.get("GROQ_API_KEY")
        self.model_name = model_name or ConfigManager.get("MODEL_NAME", "Llama3-8b-8192")

    def initialize_llm(self):
        try:
            if not self.api_key:
                logger.error("GROQ_API_KEY not found in environment variables.")
                raise EnvironmentError("Error: GROQ_API_KEY not found in environment variables.")

            logger.info(f"Initializing ChatGroq model: {self.model_name}")
            llm = ChatGroq(groq_api_key=self.api_key, model_name=self.model_name)
            logger.info(f"ChatGroq model '{self.model_name}' initialized successfully.")
            return llm

        except EnvironmentError as ee:
            logger.error(f"Environment error: {ee}")
            raise

        except ValueError as ve:
            logger.error(f"Invalid configuration for ChatGroq model: {ve}")
            raise ValueError(f"Invalid configuration for ChatGroq model: {ve}")

        except ConnectionError as ce:
            logger.error(f"Failed to connect to ChatGroq API: {ce}")
            raise ConnectionError(f"Failed to connect to ChatGroq API: {ce}")

        except Exception as e:
            logger.error(f"Unexpected error while initializing ChatGroq model: {e}")
            raise RuntimeError(f"Unexpected error while initializing ChatGroq model: {e}") from e

        finally:
            logger.info("Model Initializing process completed (success or failure).")

class WhisperModelLoader:
    def __init__(self, model_name: str = None):
        self.model_name = model_name or ConfigManager.get("WHISPER_MODEL_NAME", "base")

    def load_model(self):
        try:
            logger.info(f"Attempting to load Whisper model: {self.model_name}")
            model = whisper.load_model(self.model_name)
            logger.info(f"Whisper model '{self.model_name}' loaded successfully.")
            return model

        except ValueError as ve:
            logger.error(f"Invalid model configuration for Whisper model '{self.model_name}': {ve}")
            raise ValueError(f"Invalid Whisper model name '{self.model_name}'.") from ve

        except RuntimeError as re:
            logger.error(f"Runtime error while loading Whisper model '{self.model_name}': {re}")
            raise RuntimeError(f"Runtime error while loading Whisper model '{self.model_name}'.") from re

        except Exception as e:
            logger.error(f"Unexpected error while loading Whisper model '{self.model_name}': {e}")
            raise RuntimeError(f"Unexpected error while loading Whisper model: {e}") from e
    
        finally:
            logger.info("Model Loading process completed (success or failure).")