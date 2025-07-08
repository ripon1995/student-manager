from django.http.response import Http404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

from student_manager.utils.custom_global_exceptions import InvalidUUIDException
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
    }, status=status.HTTP_400_BAD_REQUEST)


def format_http404_errors(exc):
    return Response({
        'status': ErrorType.NOT_FOUND.value,
        'status_code': status.HTTP_404_NOT_FOUND,
        'errors': exc if hasattr(exc, 'detail') else str(exc)
    }, status=status.HTTP_404_NOT_FOUND)


def format_generic_error(exc):
    return Response({
        'detail': ErrorType.INTERNAL_ERROR.value,
        'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def format_invalid_uuid_exception(exc):
    return Response({
        'status': exc.default_code,
        'status_code': exc.status_code,
        'errors': str(exc)
    }, status=status.HTTP_400_BAD_REQUEST)


def custom_exception_handler(exc, context):
    if isinstance(exc, ValidationError):
        return format_validation_errors(exc)

    elif isinstance(exc, Http404):
        return format_http404_errors(exc)

    elif isinstance(exc, InvalidUUIDException):
        return format_invalid_uuid_exception(exc)

    else:
        return format_generic_error(exc)
