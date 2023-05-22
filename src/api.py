from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.common.exceptions import ApiException
from src.config import get_settings
from src.ping.controllers import router as ping_router


async def api_exception_handler(req: Request, exc: ApiException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status_code": exc.status_code,
            "error_code": exc.error_code,
            "timestamp": exc.timestamp,
            "detail": exc.detail,
        },
    )


def configure_api() -> FastAPI:
    settings = get_settings()
    api = FastAPI(
        title=settings.app_title,
        description=settings.app_description,
        exception_handlers={ApiException: api_exception_handler},
    )

    api.include_router(ping_router, prefix="/ping")

    return api


api = configure_api()
