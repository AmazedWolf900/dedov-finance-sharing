from flask import Blueprint

bp = Blueprint('payments', __name__)

from app.blueprints.payments import routes