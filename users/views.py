from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from core.views import ErrorResponse, NavyaAuthLessView, SuccessResponse
from users.serializers import (
    TokenPairObtainSerializer,
    TokenRefreshSerializer,
    UserSerializer,
)


# Create your views here.
class UserRegistrationView(NavyaAuthLessView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return ErrorResponse(
                success=False, error=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return SuccessResponse(
            success=True, data=serializer.data, status=status.HTTP_201_CREATED
        )


class TokenPairObtainView(NavyaAuthLessView):
    serializer_class = TokenPairObtainSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return ErrorResponse(
                success=False, error=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        user = serializer.validated_data
        # now get the token pair
        refresh = RefreshToken.for_user(user)
        return SuccessResponse(
            success=True,
            data={"access": str(refresh.access_token), "refresh": str(refresh)},
            status=status.HTTP_200_OK,
        )


class RefreshTokenObtainView(NavyaAuthLessView):
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # we could have returned here with this approach, but for the sake of uniformity, lets not throw exceptions but return the ErrorResponse
        # serializer.is_valid(raise_exception=True)
        if not serializer.is_valid():
            return ErrorResponse(
                success=False,
                data=None,
                status=status.HTTP_400_BAD_REQUEST,
                error=serializer.errors,
            )
        return SuccessResponse(
            success=True,
            data={"access": str(serializer.validated_data.access_token)},
            status=status.HTTP_200_OK,
        )
