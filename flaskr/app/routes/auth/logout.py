from flask import Blueprint, redirect
from flask_login import login_required, logout_user

logout_bp = Blueprint("logout_bp",__name__, template_folder='templates')

@logout_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")