import sys

# setting path
sys.path.append('../app')


import os
import json
from flask import Flask
from flask import render_template, request, redirect, flash

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

def create_app():
    app = Flask(__name__)

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
    @login_required
    def index():
        
        # Get events and event posts
        events = db.session.execute(select(Event)).all()
            
        return render_template('index.html', events = events)

    @app.route("/login", methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect("/")
        loginForm = LoginForm(request.form)
        if loginForm.validate_on_submit():
            username = loginForm.username.data
            password = loginForm.password.data
            user = db.session.query(User).filter_by(username=username).first()
            if user is not None and user.check_password(password):
                logUser(user)
                return redirect('/')
            else:
                loginForm.message = "Impossible de se connecter"
            
        return render_template('login.html', form = loginForm)

    @app.route("/register", methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect("/")
        registerForm = RegisterForm(request.form)
        if registerForm.validate_on_submit():
            secretCode = registerForm.secretCode.data
            if secretCode == os.environ['REGISTER_SECRET_CODE']:
                username = registerForm.username.data
                password = registerForm.password.data
                # Check if user exsits in db
                user = db.session.query(User).filter_by(username=username).first()
                if user is not None:
                    registerForm.message = "Ce nom d'utilisateur.trice existe déjà"
                else:
                    newUser = User(username=username)
                    newUser.set_password(password)
                    db.session.add(newUser)
                    db.session.commit()
                    logUser(newUser)
                    return redirect('/')
            elif request.method == "POST":
                registerForm.message = "Le code secret n'est pas valide"
        elif request.method == "POST":
            registerForm.message = "Tous les champs doivent être remplis"
        return render_template("register.html", form = registerForm)

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect("/")

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
        
    def logUser(user):
        user.is_authenticated = True
        login_user(user,remember=True)
        
    
    return app