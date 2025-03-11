from flask import Blueprint, render_template, request
from flask_login import login_required
from app.database.db import db
from sqlalchemy import select
from app.models.Event import Event
from app.forms.addAttendee import AddAttendeeForm

index_bp = Blueprint("index_bp", __name__,template_folder='templates', url_prefix='/event')

@index_bp.route("/")
@login_required
def index():
    # Get events and event posts
    events = db.session.execute(select(Event)).all()
    addAttendeeForm = AddAttendeeForm(request.form)
    return render_template('index.html', events = events, addAttendeeForm = addAttendeeForm)