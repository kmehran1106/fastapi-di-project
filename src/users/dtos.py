from pydantic import BaseModel

from src.common.responses import ApiResponse


class UserDto(BaseModel):
    id: int
    name: str
    email: str


class CreateUserQuery(BaseModel):
    name: str
    email: str
    password: str


class GetUserResponse(ApiResponse):
    data: UserDto
