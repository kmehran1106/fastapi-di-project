from tests.conftest import client


def test_check_health() -> None:
    # Given

    # When
    response = client.get("/ping")
    data = response.json()

    # Then
    assert data == {"app_name": "Testing!", "message": "Healthy!"}
