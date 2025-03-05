from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column
from models.Base import Base
from datetime import date

class Event(Base):
    __tablename__ = "events"
    id: Mapped[int] = mapped_column(primary_key=True)
    eventName: Mapped[str] = mapped_column(String(250))
    date = mapped_column(Date)
