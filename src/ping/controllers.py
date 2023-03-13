from fastapi import APIRouter, Depends

from src.common.enums import ErrorCode
from src.common.exceptions import ApiException
from src.ping.dtos import CheckHealthResponse, HealthDto
from src.ping.services import check_health

router = APIRouter()


@router.get("/")
async def check_health_api(
    fail: int = 0,
    check_health: HealthDto = Depends(check_health),
) -> CheckHealthResponse:
    if fail != 0:
        raise ApiException(status_code=400, error_code=ErrorCode.INVALID.value, detail="You shall not pass!")
    return CheckHealthResponse(data=check_health, status_code=200)
