from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import Session

from src.common.db import Base
from src.common.security import get_password_hash
from src.users.dtos import CreateUserQuery


class UserModel(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    hashed_password = Column(String, nullable=False)

    __tablename__ = "users"


class UserRepository:
    def get(self, db: Session, *, id: int) -> UserModel:
        return db.query(UserModel).filter(UserModel.id == id).first()

    def create(self, db: Session, *, query: CreateUserQuery) -> UserModel:
        _user = UserModel(
            name=query.name,
            email=query.email,
            hashed_password=get_password_hash(query.password),
        )
        db.add(_user)
        db.commit()
        db.refresh(_user)
        return _user


user_repository = UserRepository()
