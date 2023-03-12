from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI DI"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
