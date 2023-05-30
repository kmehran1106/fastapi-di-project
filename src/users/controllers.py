from fastapi import APIRouter, Depends

from src.users.dtos import GetUserResponse, UserDto
from src.users.services import get_user

router = APIRouter()


@router.get("/{user_id}")
async def get_user_api(get_user: UserDto = Depends(get_user)) -> GetUserResponse:
    return GetUserResponse(data=get_user, status_code=200)
