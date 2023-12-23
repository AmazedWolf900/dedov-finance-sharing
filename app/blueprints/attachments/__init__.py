from flask import Blueprint

bp = Blueprint('attachments', __name__)

from app.blueprints.attachments import routes