from typing import Optional

from pydantic import BaseModel, Field


class GenderBase(BaseModel):
    id: int = Field(...)
    name: str = Field(...)

    class Config:
        orm_mode = True


class CreateGender(BaseModel):
    name: str = Field(...)


class SearchGender(BaseModel):
    id: Optional[int] = Field(None)
    name: Optional[str] = Field(None)


class UpdateGender(BaseModel):
    name: Optional[str] = Field(None)
