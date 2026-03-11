from .app import create_app
from .extensions import db
from .models import Student, Assignment, Grade

app = create_app()

# This file exists so that we can run commands like:
# flask --app manage_migrations db init
# flask --app manage_migrations db migrate -m "initial schema"
# flask --app manage_migrations db upgrade

if __name__ == "__main__":
    app.run(debug=True)