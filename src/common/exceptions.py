from datetime import datetime

from fastapi import HTTPException


class ApiException(HTTPException):
    def __init__(self, status_code: int, error_code: str, detail: str):
        super().__init__(status_code=status_code, detail=detail)
        self.error_code = error_code
        self.timestamp = datetime.utcnow().isoformat()
