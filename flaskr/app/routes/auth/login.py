from flask import Blueprint
from flask import render_template, request, redirect
from flask_login import  current_user
from app.models.User import User
from app.forms.loginForm import LoginForm
from app.database.db import db
from app.services.auth import logUser

login_bp = Blueprint('login_bp', __name__, template_folder='templates')

@login_bp.route("/login", methods=['GET', 'POST'])
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

