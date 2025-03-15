import json
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required
from app.database.db import db
from sqlalchemy import select
from app.models.Event import Event
from app.models.EventPost import EventPost
from app.forms.addAttendee import AddAttendeeForm
from app.forms.newEventPost import NewEventPost

eventPost_bp = Blueprint("eventPost_bp", __name__)

@eventPost_bp.route("/event/<eventId>/post/new",methods=["GET","POST"])
@login_required
def newPost(eventId):
    form = NewEventPost(request.form)
    if form.validate_on_submit() and request.method=="POST":
        eventPost = EventPost(event_id = eventId, name = form.name.data)
        if form.start_time.data:
            eventPost.start_time = form.start_time.data
        if form.end_time.data:
            eventPost.end_time = form.end_time.data
        resp = saveEventPost(eventPost)
        if resp.status_code == 500:
            flash("La création d'un nouveau poste a échoué")
        # return resp
    return redirect("/")

@eventPost_bp.route("/post/<eventPostId>/addAttendee",methods=["GET","POST"])
@login_required
def addAttendee_Post(eventPostId):
    form = AddAttendeeForm(request.form)
    if form.validate_on_submit() and request.method =="POST":
        eventPost = db.session.query(EventPost).filter_by(id=eventPostId).first()
        eventPost.add_attendee(form.name.data)
        resp = saveEventPost(eventPost)
        if resp.status_code == 500:
            flash("L'ajout d'une personne a échoué")
        # return resp
    return redirect("/")


@eventPost_bp.route("/post/<eventPostId>/attendee/<attendeeId>/destroy", methods=['DELETE'])
@login_required
def deleteAttendee_Delete(eventPostId, attendeeId):
    eventPost = db.session.query(EventPost).filter_by(id=eventPostId).first()
    eventPost.remove_attendee(attendeeId)
    resp = saveEventPost(eventPost)
    if resp.status_code == 500:
        flash("La suppression a échoué")
    return resp

@eventPost_bp.route("/post/<postId>/delete", methods=["DELETE"])
@login_required
def deleteEventPost(postId):
    eventPost = db.session.query(EventPost).filter_by(id=postId).delete()
    try:
        db.session.commit()
        resp = jsonify(success=True)
    except:
        print("ERREUR")
        resp = jsonify(message=""), 500
    if resp.status_code == 500:
        flash("La suppression a échoué")
    print(resp.status_code, flush=True)
    return resp

def saveEventPost(eventPost):
    db.session.add(eventPost)
    try:
        db.session.commit()
        resp = jsonify(success=True)
    except:
        resp = jsonify(message=""), 500
    return resp