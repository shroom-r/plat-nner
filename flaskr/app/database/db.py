from flask_sqlalchemy import SQLAlchemy
from app.models.Base import Base
from app.models.Event import Event
from app.models.EventPost import EventPost
from app.models.User import User
from sqlalchemy import event

from app.models.User import User

db = SQLAlchemy(model_class=Base)