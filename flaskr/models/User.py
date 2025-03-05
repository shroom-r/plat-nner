from sqlalchemy import Integer, String, Text, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column
from models.Base import Base
from werkzeug.security import generate_password_hash, check_password_hash
import os

class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(250), unique=True)
    salt = mapped_column(LargeBinary)
    password_hash = mapped_column(Text)


    def set_password(self, password):
        # Generate salt
        self.salt = os.urandom(32)
        self.password_hash = generate_password_hash(f'{self.salt}{password}')

    def check_password(self, password):
        return check_password_hash(self.password_hash, f'{self.salt}{password}')