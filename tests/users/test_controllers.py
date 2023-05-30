from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.users.dtos import CreateUserQuery, GetUserResponse, UserDto
from src.users.repositories import user_repository


def test_get_user_api_success(client: TestClient, db: Session) -> None:
    # Given
    user = user_repository.create(db, query=CreateUserQuery(name="name", email="email", password="password"))

    # When
    response = client.get(f"/users/{user.id}")
    result = response.json()
    expected = jsonable_encoder(
        GetUserResponse(status_code=200, data=UserDto(id=user.id, name=user.name, email=user.email)),
    )

    # Then
    assert result == expected
