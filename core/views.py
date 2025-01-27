from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


class AuthByTokenMixin:
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class AuthByNoneMixin:
    authentication_classes = []
    permission_classes = []


class NavyaAuthLessView(AuthByNoneMixin, GenericAPIView):
    pass


class NavyaAuthView(AuthByTokenMixin, GenericAPIView):
    pass


class NavyaSuperUserView(AuthByTokenMixin, GenericAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]


class SuccessResponse(Response):
    def __init__(self, data=None, success=True, status=None, message=None, **kwargs):
        super().__init__(
            {"success": success, "data": data, "status": status, "message": message},
            status=status,
            **kwargs,
        )


class ErrorResponse(Response):
    def __init__(self, data=None, success=False, status=None, error=None, **kwargs):
        super().__init__(
            {"success": success, "data": data, "error": error, "status": status},
            status=status,
            **kwargs,
        )
