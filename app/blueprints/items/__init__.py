from flask import Blueprint

bp = Blueprint('items', __name__)

from app.blueprints.items import routes