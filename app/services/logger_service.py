# app\services\logger_service.py

import logging

class LoggerService:
    
    _loggers = {}

    @classmethod
    def get_logger(cls, name=__name__):
        if name not in cls._loggers:
            logger = logging.getLogger(name)
            logger.setLevel(logging.INFO)

            if not logger.handlers:
                console_handler = logging.StreamHandler()
                console_handler.setLevel(logging.INFO)

                formatter = logging.Formatter(
                    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                )
                console_handler.setFormatter(formatter)
                logger.addHandler(console_handler)
            
            cls._loggers[name] = logger
        
        return cls._loggers[name]
