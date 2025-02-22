from sqlalchemy import Column, Integer, String

from app.db.base import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    current_status = Column(String)
