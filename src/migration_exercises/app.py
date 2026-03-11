import os
from flask import Flask

from .config import Config, DATA_DIR
from .extensions import db, migrate
from .routes import api


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    os.makedirs(DATA_DIR, exist_ok=True)

    # TODO 1:
    # Initialize the SQLAlchemy extension with the app.


    # TODO 2:
    # Initialize Flask-Migrate with the app and database.


    app.register_blueprint(api, url_prefix="/exercises")

    return app