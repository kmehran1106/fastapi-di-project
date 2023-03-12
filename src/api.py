from fastapi import FastAPI

from src.ping.controllers import router as ping_router


def configure_api() -> FastAPI:
    api = FastAPI()

    api.include_router(ping_router, prefix="/ping")

    return api
