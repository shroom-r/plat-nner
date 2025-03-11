import json
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from app.database.db import db
from sqlalchemy import select
from app.models.Event import Event
from app.models.EventPost import EventPost
from app.forms.addAttendee import AddAttendeeForm

eventPost_bp = Blueprint("eventPost_bp", __name__)


@eventPost_bp.post("/event/<postId>/post/<eventPostId>/addAttendee")
@login_required
def addAttendee_Post(postId, eventPostId):
    form = AddAttendeeForm(request.form)
    if form.validate_on_submit():
        eventPost = db.session.query(EventPost).filter_by(id=eventPostId).first()
        eventPost.add_attendee(form.name.data)
        db.session.add(eventPost)
        try:
            db.session.commit()
            resp = jsonify(success=True)
        except:
            resp = jsonify(message="Erreur lors de l'ajout d'une personne"), 500
        return resp

@eventPost_bp.delete("/event/<postId>/post/<eventPostId>/removeAttendee/<attendeeId>/destroy")
@login_required
def destroyAttendee_Delete(eventPostId, attendeeId):
    pass