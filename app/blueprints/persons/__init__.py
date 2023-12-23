from flask import Blueprint

bp = Blueprint('persons', __name__)

from app.blueprints.persons import routes