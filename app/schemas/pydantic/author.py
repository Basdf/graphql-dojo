from typing import List, Optional

from pydantic import BaseModel, Field

from app.schemas.pydantic.gender import CreateGender, GenderBase, SearchGender


class AuthorBase(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    genders: List[GenderBase] = Field(...)


class CreateAuthor(BaseModel):
    name: str = Field(...)
    genders: List[CreateGender] = Field(...)


class SearchAuthor(BaseModel):
    name: Optional[str] = Field(None)
    genders: List[SearchGender] = Field(None)


class UpdateAuthor(BaseModel):
    name: Optional[str] = Field(None)
