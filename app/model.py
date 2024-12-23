# app\model.py
import os
import whisper
from logger import get_logger
from langchain_groq import ChatGroq  # type: ignore
from config import GROQ_API_KEY



logger = get_logger(__name__)

def initialize_llm():
    try:
        if not GROQ_API_KEY:
            logger.error("GROQ_API_KEY not found in environment variables.")
            raise EnvironmentError("Error: GROQ_API_KEY not found in environment variables.")

        llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name="Llama3-8b-8192")
        logger.info("ChatGroq model initialized successfully.")
        return llm

    except Exception as e:
        logger.error(f"Error initializing the ChatGroq model: {e}")
        raise ConnectionError(f"Error initializing the ChatGroq model: {e}")

def load_whisper_model(model_name="base"):
    try:
        logger.info(f"Attempting to load Whisper model: {model_name}")
        model = whisper.load_model(model_name)
        logger.info(f"Whisper model '{model_name}' loaded successfully.")
        return model
    except Exception as e:
        logger.error(f"Failed to load Whisper model '{model_name}': {str(e)}")
        raise RuntimeError(f"Error loading Whisper model '{model_name}'.") from e

