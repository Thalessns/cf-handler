"""Tables related to database operations."""
from datetime import datetime
from sqlalchemy import Column, String, Integer
from uuid import uuid4

from src.database.database import Base


class Tag(Base):
    """Database table for tags."""

    __tablename__ = "tag"

    id = Column(String, primary_key=True, index=True)
    key = Column(String, nullable=False, default=str(uuid4()))
    first_use = Column(String, nullable=False, default=datetime.now().isoformat())
    last_use = Column(String, nullable=False, default=datetime.now().isoformat())


class History(Base):
    """Database table for tag usage history."""

    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tag_id = Column(String, nullable=False, foreign_key="tag.id")
    timestamp = Column(String, nullable=False, default=datetime.now().isoformat())


tag_table = Tag.__table__
history_table = History.__table__
