import uuid
from .custom_global_exceptions import InvalidUUIDException


def validate_uuid(uuid_string):
    try:
        return uuid.UUID(str(uuid_string))
    except ValueError:
        raise InvalidUUIDException