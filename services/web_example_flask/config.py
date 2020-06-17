import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True
UPLOAD_PATH = ''

# Flask variables
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/application/static"
TEMPLATES_FOLDER = f"{os.getenv('APP_FOLDER')}/application/templates"
