from flask import Blueprint, render_template
from logger import get_logger

logger = get_logger(__name__)

home_bp = Blueprint('home', __name__)

@home_bp.route("/")
def home():
    logger.info("Rendering home page")
    return render_template("index.html")
