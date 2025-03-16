from app.database.db import db
from sqlalchemy import select
from app.models.Event import Event

from datetime import date, timedelta

def deletePastEventsAndCreateNew():
    events = db.session.execute(select(Event)).all()
    today = date.today()
    # Delete past events
    for eventObj in events:
        event = eventObj[0]
        if event.date < today:
            db.session.delete(event)

    # Add new events every wednesday for next 7 weeks when missing
    # existingEvents = db.session.execute(select(Event)).all()
    nextWednesday = getNextWeekday(today, 2)
    newEvents = []
    for i in range(7):
        newEvents.append(
            Event(date= nextWednesday, name = "Repas mercredi")
        )
        nextWednesday = nextWednesday + timedelta(7)

    for event in newEvents:
        db.session.add(event)

    db.session.commit()

def getNextWeekday(refDate, weekday):
    days_ahead = weekday - refDate.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return refDate + timedelta(days_ahead)