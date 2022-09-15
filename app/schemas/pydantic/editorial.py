from typing import Optional

from pydantic import BaseModel, Field


class EditorialBase(BaseModel):
    id: int = Field(...)
    name: str = Field(...)

    class Config:
        orm_mode = True


class CreateEditorial(BaseModel):
    name: str = Field(...)


class SearchEditorial(BaseModel):
    id: Optional[int] = Field(None)
    name: Optional[str] = Field(None)


class UpdateEditorial(BaseModel):
    name: Optional[str] = Field(None)
