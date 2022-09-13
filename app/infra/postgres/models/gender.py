from sqlalchemy import Column, Integer, Sequence, String

from app.core.db import Base


class Gender(Base):
    __tablename__ = "gender"
    id = Column(Integer, Sequence("gender_id_seq"), primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return f"<Gender(name='{self.name}')>"
