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
        
    # def get_attendees_names(self):
    #     attendees = self.get_attendees()
    #     if attendees:
    #         return [attendee['name'] for attendee in attendees]
    
    def set_attendees(self, attendeesArr):
        dict = {}
        dict['data'] = attendeesArr
        self.attendees = json.dumps(dict)
        
    def add_attendee(self, name):
        attendees = self.get_attendees()
        newId = 0
        if attendees:
            maxId = max(attendees, key=lambda x:x['id'])['id']
            newId = maxId + 1
        attendees.append({'id' : newId, 'name' : name})
        self.set_attendees(attendees)
    
    def remove_attendee(self, id):
        attendees = self.get_attendees()
        # Remove attendee by value
        newAttendees = [attendee for attendee in attendees if str(attendee['id']) != id]
        self.set_attendees(newAttendees)

    
    def get_time_string(self):
        start = self.start_time.strftime('%H:%M') if self.start_time else ""
        end = self.end_time.strftime('%H:%M') if self.end_time else ""
        if not start and not end:
            return ""
        else:
            return str(start) + "-" + str(end)