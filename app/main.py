# app\main.py

import os
import warnings
from flask import Flask # type: ignore
from app.services.logger_service import LoggerService

from app.routes.home_routes import home_bp
from app.routes.upload_routes import upload_bp
from app.routes.error_routes import error_bp

warnings.filterwarnings("ignore", category=UserWarning, message=".*FP16 is not supported.*")
warnings.filterwarnings("ignore", category=FutureWarning, message=".*torch.load.*")

logger = LoggerService.get_logger(__name__)

warnings.filterwarnings("ignore", category=UserWarning, message=".*torch.load.*")

def create_app():
    app = Flask(__name__)

    UPLOAD_FOLDER = "uploads"
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

    app.register_blueprint(home_bp)
    app.register_blueprint(upload_bp)
    app.register_blueprint(error_bp)

    return app
