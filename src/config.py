import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "FastAPI DI"
    app_description: str = "Trying out Dependency Injection with FastAPI!"
    sqlalchemy_url: str = os.getenv("SQLALCHEMY_URL", default="postgresql://fastdi:fastdi@db/fastdi")


@lru_cache()
def get_settings() -> Settings:
    return Settings()
