from sqlalchemy import Column, Integer, Sequence, String

from app.core.db import Base


class Editorial(Base):
    __tablename__ = "editorial"
    id = Column(Integer, Sequence("editorial_id_seq"), primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return f"<Editorial(name='{self.name}')>"
