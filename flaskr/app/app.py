from flask import Flask
from markupsafe import escape
from flask import render_template
from database.db import db
import os
# Import models to create tables in database
from config import TestingConfig, ProductionConfig, DevelopmentConfig
from flask_migrate import Migrate

def load_models():
    from models.User import User
    from models.Event import Event
    from models.EventPost import EventPost

# Define applications
app = Flask(__name__)


env = 'testing'
try:
    env = os.environ['FLASK_ENV']
except KeyError:
    pass

if env == 'development':
    config = DevelopmentConfig()
elif env=='production':
    config = ProductionConfig()
else:
    config = TestingConfig()


# Configure connection to database
# with open(os.environ.get("DATABASE_PASSWORD_FILE"), "r") as f:
#     databasePassword = f.read()
#     app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://root:{databasePassword}@db/plat_nner_db"
app.config.from_object(config)

# db = SQLAlchemy(app)
db.init_app(app)



# with app.app_context():
#     db.create_all()

load_models()

migrate = Migrate(app, db)



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/user/<name>")
def hello(name):
    return f'Hello, {escape(name).capitalize()}'
