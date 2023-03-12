from unittest.mock import Mock

import pytest

from src.config import Settings, get_settings
from src.ping.services import check_health
from tests.conftest import api


@pytest.mark.asyncio
async def test_check_health_with_fixture(mock_settings: Settings) -> None:
    # Given
    mock_settings.app_name = "Testing!"

    # When
    data = await check_health(mock_settings)

    # Then
    assert data == {"app_name": "Testing!", "message": "Healthy!"}


@pytest.mark.asyncio
async def test_check_health_with_dependency() -> None:
    # Given
    mock_settings = Mock(spec=Settings)
    mock_settings.app_name = "Testing!"
    api.dependency_overrides[get_settings] = mock_settings

    # When
    data = await check_health(mock_settings)

    # Then
    assert data == {"app_name": "Testing!", "message": "Healthy!"}
    del api.dependency_overrides[get_settings]
