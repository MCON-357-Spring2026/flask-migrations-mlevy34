import os
from flask import Flask
from .config import Config
from .extensions import db, migrate
from .routes import api


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    # Load configuration from the Config class in config.py
    app.config.from_object(Config)
    # Ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)
    # Initialize extensions

    # database instance is created in extensions.py and imported here,
    # so we just call db.init_app(app) to initialize it with the Flask app.
    db.init_app(app)
    # migrate instance is created in extensions.py and imported here,
    migrate.init_app(app, db)
    # Register blueprints (routes)
    app.register_blueprint(api)

    return app