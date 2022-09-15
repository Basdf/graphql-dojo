from typing import List, Optional

from pydantic import BaseModel, Field

from app.schemas.pydantic.editorial import EditorialBase
from app.schemas.pydantic.gender import CreateGender, GenderBase, SearchGender


class BookBase(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    editorial: EditorialBase = Field(...)
    genders: List[GenderBase] = Field(...)

    class Config:
        orm_mode = True


class CreateBook(BaseModel):
    name: str = Field(...)
    editorial_id: int = Field(...)
    genders: List[CreateGender] = Field(...)


class SearchBook(BaseModel):
    id: Optional[int] = Field(None)
    name: Optional[str] = Field(None)
    editorial_id: Optional[int] = Field(None)


class UpdateBook(BaseModel):
    name: Optional[str] = Field(None)
    editorial_id: Optional[int] = Field(None)
