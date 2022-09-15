from typing import List, Optional

from pydantic import BaseModel, Field

from app.schemas.pydantic.gender import CreateGender, GenderBase, SearchGender


class AuthorBase(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    genders: List[GenderBase] = Field(...)

    class Config:
        orm_mode = True


class CreateAuthor(BaseModel):
    name: str = Field(...)
    genders: List[CreateGender] = Field(...)


class SearchAuthor(BaseModel):
    id: Optional[int] = Field(None)
    name: Optional[str] = Field(None)


class UpdateAuthor(BaseModel):
    name: Optional[str] = Field(None)
