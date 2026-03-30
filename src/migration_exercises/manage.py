from .extensions import db
from .models import Student, Assignment, Grade
from src.migration_exercises.app import db
from src.migration_exercises import models
from .app import create_app
app = create_app()

# TODO 3:





if __name__ == "__main__":
    app.run(debug=True)