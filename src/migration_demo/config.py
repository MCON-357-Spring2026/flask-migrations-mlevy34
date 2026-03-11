"""
Configuration for the Flask application, including database URI and other settings.
Compare to the flask_orm where we put the configuration in the app.py and used app.config.from_mapping.
Here we have a separate config.py file and we will import the Config class in app.py and use it there.
"""
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DB_PATH = os.path.join(DATA_DIR,  "gradebook_migrations.db")


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", f"sqlite:///{DB_PATH}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False