from fastapi import APIRouter, Depends

from src.ping.dtos import CheckHealthDto
from src.ping.services import check_health

router = APIRouter()


@router.get("/", response_model=CheckHealthDto)
async def check_health_api(check_health: CheckHealthDto = Depends(check_health)) -> CheckHealthDto:
    return check_health
