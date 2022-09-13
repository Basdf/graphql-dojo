from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, Sequence("author_id_seq"), primary_key=True)
    name = Column(String(50))
    genders = relationship(
        "Gender",
        secondary="author_x_gender",
        backref="authors",
        cascade="save-update, merge",
    )

    def __repr__(self):
        return f"<Author(name='{self.name}')>"
