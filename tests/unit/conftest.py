from typing import Generator, cast
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

from src.api import configure_api
from src.common.db import Base
from src.common.session import SessionLocal
from src.config import Settings, get_settings

# NOTE: FOR FASTAPI CONTROLLER BASED CHECKS


api = configure_api()


def get_settings_override() -> Settings:
    return Settings(app_title="Testing!")


api.dependency_overrides[get_settings] = get_settings_override


@pytest.fixture(scope="session")
def mock_settings() -> Settings:
    return cast(Settings, Mock(spec=Settings))


@pytest.fixture(scope="session")
def settings() -> Settings:
    return Settings()


@pytest.fixture(scope="session")
def engine(settings: Settings) -> Engine:
    return create_engine(settings.sqlalchemy_url, echo=False, connect_args={"connect_timeout": 30})


@pytest.fixture(autouse=True)
def db(engine: Engine) -> Generator[Session, None, None]:
    Base.metadata.drop_all(bind=engine)  # type: ignore
    Base.metadata.create_all(bind=engine)  # type: ignore

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(api) as c:
        yield c
