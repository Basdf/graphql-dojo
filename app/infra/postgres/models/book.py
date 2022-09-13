from sqlalchemy import Column, ForeignKey, Integer, Sequence, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, Sequence("book_id_seq"), primary_key=True)
    name = Column(String(50))
    editorial_id = Column(ForeignKey("editorial.id", ondelete="CASCADE"))
    editorial = relationship(
        "Editorial",
        backref="books",
        passive_deletes=True,
        cascade="save-update, merge",
        lazy="subquery",
    )
    genders = relationship(
        "Gender",
        secondary="book_x_gender",
        backref="books",
        cascade="save-update, merge",
        lazy="subquery",
    )

    def __repr__(self):
        return f"<Book(name='{self.name}')>"
