from sqlalchemy import String, Time, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.models.Base import Base
import json

class EventPost(Base):
    __tablename__ = "eventposts"
    id:Mapped[int] = mapped_column(primary_key = True)
    event_id= mapped_column(ForeignKey('events.id', ondelete='CASCADE'), nullable = False)
    name = mapped_column(String(250))
    start_time = mapped_column(Time)
    end_time = mapped_column(Time)
    attendees = mapped_column(JSON)

    def get_attendees(self):
        if self.attendees:
            return json.loads(self.attendees)['data']
        else:
            return []
    
    def get_time_string(self):
        start = self.start_time.strftime('%H:%M') if self.start_time else ""
        end = self.end_time.strftime('%H:%M') if self.end_time else ""
        if not start and not end:
            return ""
        else:
            return str(start) + "-" + str(end)