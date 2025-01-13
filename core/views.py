from rest_framework.generics import GenericAPIView
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication

class AuthByTokenMixin(object):
    authentication_classes = (JWTAuthentication)
    permission_classes = [IsAuthenticated]


class AuthByNoneMixin(object):
    authentication_classes = []
    permission_classes = []

class NavyaAuthLessView(AuthByNoneMixin, GenericAPIView):
    pass


class NavyaAuthView(AuthByTokenMixin, GenericAPIView):
    pass


class SuccessResponse(Response):
    def __init__(self, data=None, success=True, status=None, message=None, **kwargs):
        super().__init__(
            {"success": success, "data": data, "status": status, "message": message}, status=status, **kwargs
        )


class ErrorResponse(Response):
    def __init__(self, data=None, success=False, status=None, error=None, **kwargs):
        super().__init__({"success": success, "data": data, "error": error, "status": status}, status=status, **kwargs)