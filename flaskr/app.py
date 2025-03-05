from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template
from database.db import db
import os
# Import models to create tables in database
from models.User import User
from models.Event import Event

# Define applications
app = Flask(__name__)

# Configure connection to database
databasePassword = open(os.environ.get("DATABASE_PASSWORD_FILE"), "r").read()
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://root:{databasePassword}@db/example"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/user/<name>")
def hello(name):
    return f'Hello, {escape(name).capitalize()}'
