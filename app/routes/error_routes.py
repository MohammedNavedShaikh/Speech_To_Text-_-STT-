from flask import Blueprint, render_template
from logger import get_logger

logger = get_logger(__name__)
error_bp = Blueprint('error', __name__)

@error_bp.app_errorhandler(404)
def not_found(error):
    logger.warning("404 error encountered: Page not found.")
    return render_template("404.html"), 404
