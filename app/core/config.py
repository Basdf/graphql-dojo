from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    TITLE: str = Field(...)
    VERSION: str = Field(...)
    DESCRIPTION: str = Field(...)
    ENVIRONMENT: str = Field(...)
    DATABASE_URL: str = Field(...)


settings = Settings()
