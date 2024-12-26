# config.py
import os
from dotenv import load_dotenv # type: ignore

class ConfigManager:

    _config = None

    @classmethod
    def load_config(cls):
        if cls._config is None:
            load_dotenv()
            cls._config = {
                "GROQ_API_KEY": os.getenv("GROQ_API_KEY"),
                "MODEL_NAME": os.getenv("MODEL_NAME", "Llama3-8b-8192"),
                "WHISPER_MODEL_NAME": os.getenv("WHISPER_MODEL_NAME", "base"),
                "ALLOWED_LANGUAGES": os.getenv("ALLOWED_LANGUAGES", "en,hi")
            }
        return cls._config

    @classmethod
    def get(cls, key, default=None):
        if cls._config is None:
            cls.load_config()
        return cls._config.get(key, default)
