from sqlalchemy.orm import Session

from src.users.dtos import CreateUserQuery
from src.users.repositories import UserModel, user_repository


def test_create_user(db: Session) -> None:
    # Given

    # When
    user = user_repository.create(db, query=CreateUserQuery(name="name", email="email", password="password"))

    # Then
    assert isinstance(user, UserModel)
    assert user.name == "name"
    assert user.email == "email"


def test_get_user(db: Session) -> None:
    # Given
    created = user_repository.create(db, query=CreateUserQuery(name="name", email="email", password="password"))

    # When
    returned = user_repository.get(db, id=created.id)

    # Then
    assert isinstance(returned, UserModel)
    assert returned.name == created.name
    assert returned.email == created.email
    assert returned.id == created.id
