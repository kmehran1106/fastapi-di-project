from sqlalchemy.orm import Session

from src.users.dtos import CreateUserQuery, UserDto
from src.users.repositories import UserModel, user_repository
from src.users.services import get_user


def test_get_user(db: Session) -> None:
    # Given
    created: UserModel = user_repository.create(
        db, query=CreateUserQuery(name="name", email="email", password="password")
    )

    # When
    returned: UserDto = get_user(db, created.id)

    # Then
    assert returned.id == created.id
