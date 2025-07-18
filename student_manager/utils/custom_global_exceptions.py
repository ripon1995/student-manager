from rest_framework import status
from rest_framework.exceptions import APIException


class InvalidUUIDException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid UUID provided.'
    default_code = 'uuid error'
