from fastapi import Depends

from src.config import Settings, get_settings
from src.ping.dtos import CheckHealthDto


async def check_health(settings: Settings = Depends(get_settings)) -> CheckHealthDto:
    return CheckHealthDto(message="Healthy!", app_name=settings.app_name)
