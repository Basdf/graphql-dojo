from sqlalchemy import Column, ForeignKey, Integer, Sequence

from app.core.db import Base


class AuthorXGender(Base):
    __tablename__ = "author_x_gender"
    id = Column(Integer, Sequence("author_x_gender_id_seq"), primary_key=True)
    gender_id = Column(ForeignKey("gender.id", ondelete="CASCADE"), primary_key=True)
    author_id = Column(ForeignKey("author.id", ondelete="CASCADE"), primary_key=True)
