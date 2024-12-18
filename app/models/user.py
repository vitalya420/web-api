from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db import Base


class User(Base):
    __tablename__ = "users"

    phone_number: Mapped[str] = mapped_column(String, unique=True)
