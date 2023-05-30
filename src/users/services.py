from fastapi import Depends, Path
from sqlalchemy.orm import Session

from src.common.deps import get_db
from src.users.dtos import UserDto
from src.users.repositories import user_repository


def get_user(db: Session = Depends(get_db), user_id: int = Path(...)) -> UserDto:
    _user = user_repository.get(db, id=user_id)
    return UserDto(id=_user.id, name=_user.name, email=_user.email)
