from pydantic import BaseModel

from src.common.responses import ApiResponse


class HealthDto(BaseModel):
    message: str
    app_title: str


class CheckHealthResponse(ApiResponse):
    data: HealthDto
