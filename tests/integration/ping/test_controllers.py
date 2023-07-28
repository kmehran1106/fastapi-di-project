from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient

from src.common.enums import ErrorCode
from src.ping.dtos import CheckHealthResponse, HealthDto


def test_check_health_success(client: TestClient) -> None:
    # Given

    # When
    response = client.get("/ping")
    result = response.json()
    expected = jsonable_encoder(
        CheckHealthResponse(status_code=200, data=HealthDto(message="Healthy!", app_title="Testing!")),
    )

    # Then
    assert result == expected


def test_check_health_failure(client: TestClient) -> None:
    # Given

    # When
    response = client.get("/ping", params={"fail": 1})
    result = response.json()

    # Then
    assert result["status_code"] == 400
    assert result["error_code"] == ErrorCode.INVALID.value
