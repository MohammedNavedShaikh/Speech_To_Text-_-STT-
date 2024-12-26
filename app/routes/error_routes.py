# app\routes\error_routes.py

from app.services.logger_service import LoggerService
from flask import Blueprint, render_template # type: ignore

logger = LoggerService.get_logger(__name__)
error_bp = Blueprint('error', __name__)

@error_bp.app_errorhandler(404)
def not_found(error):
    logger.warning("404 error encountered: Page not found.")
    return render_template("404.html"), 404
