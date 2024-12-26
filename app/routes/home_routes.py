# app\routes\home_routes.py

from flask import Blueprint, render_template # type: ignore
from app.services.logger_service import LoggerService

logger = LoggerService.get_logger(__name__)

home_bp = Blueprint('home', __name__)

@home_bp.route("/")
def home():
    logger.info("Rendering home page")
    return render_template("index.html")
