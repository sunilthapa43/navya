from django.urls import path

from .views import UserRegistrationView, TokenPairObtainView, RefreshTokenObtainView

urlpatterns = [
    path('auth/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('auth/token/', TokenPairObtainView.as_view(), name='token-obtain-pair'),
    path('auth/refresh/', RefreshTokenObtainView.as_view(), name='token-refresh'),
]