from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.configuration import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    # Enable CORS
    CORS(app, supports_credentials=True)

    with app.app_context():
        from app import routes, models
        db.create_all()

    return app
