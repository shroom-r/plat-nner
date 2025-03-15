from flask import Blueprint, render_template, request
from flask_login import login_required
from app.database.db import db
from sqlalchemy import select
from app.models.Event import Event
from app.forms.addAttendee import AddAttendeeForm
from app.forms.deleteAttendee import DeleteAttendeeForm
from app.forms.newEventPost import NewEventPost
from app.forms.deletePost import DeletePostForm

index_bp = Blueprint("index_bp", __name__,template_folder='templates', url_prefix='/event')

@index_bp.route("/")
@login_required
def index():
    # Get events and event posts
    events = db.session.execute(select(Event)).all()
    addAttendeeForm = AddAttendeeForm(request.form)
    deleteAttendeeForm = DeleteAttendeeForm(request.form)
    newEventPostForm = NewEventPost()
    deletePostForm = DeletePostForm()

    return render_template( \
        'index.html', \
        events = events, \
        addAttendeeForm = addAttendeeForm, \
        deleteAttendeeForm = deleteAttendeeForm, \
        newEventPostForm = newEventPostForm, \
        deletePostForm = deletePostForm, \
    )