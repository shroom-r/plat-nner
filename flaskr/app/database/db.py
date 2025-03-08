from flask_sqlalchemy import SQLAlchemy
from app.models.Base import Base
from app.models.Event import Event
from app.models.EventPost import EventPost
from app.models.User import User
from sqlalchemy import event

import os
from app.models.User import User
from sqlalchemy import select

db = SQLAlchemy(model_class=Base)

def createDefaultUser():
    username = os.environ.get("DB_DEFAULT_USER")
    password = os.environ.get("DB_DEFAULT_USER_PASSWORD")

    stmt = select(User).where(User.username==username)

    result = db.session.execute(stmt)
    
    user = result.scalar()

    if not user:
        user = User(username=username)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()