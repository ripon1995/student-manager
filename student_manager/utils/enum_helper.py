from enum import Enum

class ErrorType(Enum):
    VALIDATION_ERROR = 'validation error'
    NOT_FOUND = "not found"
    INVALID_INPUT = "invalid input"
    UNAUTHORIZED = "unauthorized"
    FORBIDDEN = "forbidden"
    INTERNAL_ERROR = "internal error"

