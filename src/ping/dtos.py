from pydantic import BaseModel


class CheckHealthDto(BaseModel):
    message: str
    app_name: str
