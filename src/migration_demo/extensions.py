# compare to src/demo/extensions.py -  we adding Migrate extension to the SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(directory="src/migration_demo/migrations")