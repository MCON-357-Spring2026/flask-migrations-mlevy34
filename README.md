# Flask Migrations

This repo demonstrates how to use Flask-Migrate to manage database schema changes in a Flask application. It includes exercises to practice creating and applying migrations, as well as evolving the database schema over time. The README provides step-by-step instructions for setting up the project, running migrations, and testing the API endpoints.

## To initialize the database run from repo root:
```bash
flask --app src.migration_demo.manage:app db init 
```
Check that the `migrations/` folder is created.
## To generate a migration after making changes to the models:
```bash
flask --app src.migration_demo.manage:app db migrate -m "Initial migration"
```
Check that a new migration file is created in the `migrations/versions/` folder with the expected schema changes.
## To apply the migration to the database:
```bash
flask --app src.migration_demo.manage:app db upgrade
```
Check that sqlite3 database file is created in the data directory and that the schema matches the models defined in `app.py`. You can also test the API endpoints to confirm that the application is working as expected.

Now run the demo application:
```bash
flask --app src.migration_demo.manage:app run
```
You can test the API endpoints using curl or Postman to confirm that the application is working as