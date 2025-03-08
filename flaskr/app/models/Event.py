from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.Base import Base

class Event(Base):
    __tablename__ = "events"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250))
    date = mapped_column(Date, nullable = False)
    event_posts = relationship("EventPost", cascade="delete, delete-orphan")
