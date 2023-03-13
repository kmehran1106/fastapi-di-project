from fastapi import Depends

from src.config import Settings, get_settings
from src.ping.dtos import HealthDto


async def check_health(settings: Settings = Depends(get_settings)) -> HealthDto:
    return HealthDto(message="Healthy!", app_title=settings.app_title)
