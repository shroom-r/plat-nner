import sys

# setting path
sys.path.append('../app')


import os
import json
from flask import Flask
from flask import render_template, request, redirect, flash,url_for

from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
from markupsafe import escape
from app.database.db import db
import secrets
import os
from app.config import TestingConfig, ProductionConfig, DevelopmentConfig
from flask_migrate import Migrate
from app.forms.loginForm import LoginForm
from app.forms.registerForm import RegisterForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from sqlalchemy import select

from app.models.User import User
from app.models.Event import Event
from app.models.EventPost import EventPost

from app.routes.auth.login import login_bp
from app.routes.auth.register import register_bp
from app.routes.auth.logout import logout_bp
from app.routes.event import index_bp
from app.routes.eventPost import eventPost_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(logout_bp)
    app.register_blueprint(eventPost_bp)

    secretKey = secrets.token_urlsafe(16)
    app.secret_key = secretKey

    bootstrap = Bootstrap5(app)
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    loginManager = LoginManager()

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

    app.config.from_object(config)

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        migrate.init_app(app, db)
        loginManager.init_app(app)
        # createDefaultUser()
    # return app

    @app.route("/")
    def appIndex():
        return redirect(url_for("index_bp.index"))

    @loginManager.user_loader
    def load_user(user_id):
        id = int(user_id)
        user = db.session.query(User).filter_by(id = id).first()
        if user is not None:
            return User(username=user.username, id=user.id, is_authenticated = True)
        else:
            return None

    @loginManager.unauthorized_handler
    def redirectUnauthorizedUser():
        '''Redirects user to the login page if they are unauthorized (not logged in)'''
        return redirect("/login")
    
    return app