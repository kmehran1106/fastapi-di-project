from enum import Enum


class ErrorCode(Enum):
    INVALID = "invalid"
    NOT_FOUND = "not_found"
    UNAUTHORIZED = "unauthorized"
