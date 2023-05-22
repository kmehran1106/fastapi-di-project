from sqlalchemy import Boolean, Column, Integer, String

from src.common.db import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    hashed_password = Column(String, nullable=False)
