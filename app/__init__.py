from flask import Flask, request

from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register blueprints here
    from app.blueprints.persons import bp as persons_bp
    app.register_blueprint(persons_bp)
    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.blueprints.projects import bp as projects_bp
    app.register_blueprint(projects_bp)
    from app.blueprints.items import bp as items_bp
    app.register_blueprint(items_bp)
    from app.blueprints.payments import bp as payments_bp
    app.register_blueprint(payments_bp)
    from app.blueprints.attachments import bp as attachments_bp
    app.register_blueprint(attachments_bp)

    @app.context_processor
    def referrer():
        return {'referrer': request.referrer}

    return app