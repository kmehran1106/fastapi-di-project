from typing import cast
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from src.api import configure_api
from src.config import Settings, get_settings

# NOTE: FOR FASTAPI CONTROLLER BASED CHECKS


api = configure_api()
client = TestClient(api)


def get_settings_override() -> Settings:
    return Settings(app_title="Testing!")


api.dependency_overrides[get_settings] = get_settings_override


# NOTE: FOR REGULAR PYTEST CHECKS WITH FIXTURES


@pytest.fixture
def mock_settings() -> Settings:
    return cast(Settings, Mock(spec=Settings))
