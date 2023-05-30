from typing import Any

from sqlalchemy.orm import as_declarative


@as_declarative()
class Base:
    id: Any

    __name__: str

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        ...
