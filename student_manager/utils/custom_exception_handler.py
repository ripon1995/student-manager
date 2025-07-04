from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

from student_manager.utils.enum_helper import ErrorType


def flatten_errors(errors):
    """
    Flattens nested error dictionaries into a single dictionary.
    """
    flattened = {}
    for field, messages in errors.items():
        if isinstance(messages, list):
            for message in messages:
                flattened[field] = message
        else:
            flattened[field] = messages
    return flattened


def format_validation_errors(exc):
    return Response({
        'status': ErrorType.VALIDATION_ERROR.value,
        'status_code': status.HTTP_400_BAD_REQUEST,
        'errors': flatten_errors(exc.detail) if hasattr(exc, 'detail') else str(exc)
    }, )


def custom_exception_handler(exc, context):
    if isinstance(exc, ValidationError):
        return format_validation_errors(exc)

    else:
        # Custom handling for unhandled exceptions
        return Response({
            'detail': 'Something went wrong.',
            'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
