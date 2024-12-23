# app\app.py
import os
import warnings
from flask import Flask
from logger import get_logger

from app.routes.home_routes import home_bp
from app.routes.upload_routes import upload_bp
from app.routes.transcribe_routes import transcribe_bp
from app.routes.error_routes import error_bp

logger = get_logger(__name__)

warnings.filterwarnings("ignore", category=UserWarning, message=".*torch.load.*")

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(transcribe_bp)
app.register_blueprint(error_bp)