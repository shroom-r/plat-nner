from flask import Blueprint, render_template
from flask_login import login_required
from app.database.db import db
from sqlalchemy import select
from app.models.Event import Event

index_bp = Blueprint("index_bp", __name__,template_folder='templates')


@index_bp.route("/")
@login_required
def index():
    
    # Get events and event posts
    events = db.session.execute(select(Event)).all()
        
    return render_template('index.html', events = events)