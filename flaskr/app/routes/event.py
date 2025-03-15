from flask import Blueprint, render_template, request, flash, redirect, jsonify
from flask_login import login_required
from app.database.db import db
from sqlalchemy import select
from app.models.Event import Event
from app.forms.addAttendee import AddAttendeeForm
from app.forms.deleteAttendee import DeleteAttendeeForm
from app.forms.newEventPost import NewEventPost
from app.forms.deletePost import DeletePostForm
from app.forms.newEvent import NewEvent

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
    newEventForm = NewEvent()

    return render_template( \
        'index.html', \
        events = events, \
        addAttendeeForm = addAttendeeForm, \
        deleteAttendeeForm = deleteAttendeeForm, \
        newEventPostForm = newEventPostForm, \
        deletePostForm = deletePostForm, \
        newEventForm = newEventForm, \
    )

@index_bp.route("/event/new", methods=["GET","POST"])
@login_required
def newEvent():
    form = NewEvent(request.form)
    if form.validate_on_submit() and request.method=="POST":
        event = Event()
        # if form.start_time.data:
        #     eventPost.start_time = form.start_time.data
        # if form.end_time.data:
        #     eventPost.end_time = form.end_time.data
        resp = saveEvent(event)
        if resp.status_code == 500:
            flash("La création d'un nouveau poste a échoué")
        # return resp
    return redirect("/")

def saveEvent(event):
    db.session.add(event)
    try:
        db.session.commit()
        resp = jsonify(success=True)
    except:
        resp = jsonify(message=""), 500
    return resp