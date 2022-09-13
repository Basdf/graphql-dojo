from sqlalchemy import Column, ForeignKey, Integer, Sequence

from app.core.db import Base


class BookXGender(Base):
    __tablename__ = "book_x_gender"
    id = Column(Integer, Sequence("book_x_gender_id_seq"), primary_key=True)
    gender_id = Column(ForeignKey("gender.id", ondelete="CASCADE"), primary_key=True)
    book_id = Column(ForeignKey("book.id", ondelete="CASCADE"), primary_key=True)
