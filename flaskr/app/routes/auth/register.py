
import os
from flask import render_template, request, redirect
from flask import Blueprint

from app.database.db import db
import os
from app.forms.registerForm import RegisterForm
from flask_login import current_user

from app.models.User import User
from app.services.auth import logUser

register_bp = Blueprint('register_bp', __name__, template_folder='templates')

@register_bp.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index_bp.index"))
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