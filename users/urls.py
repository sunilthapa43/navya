from django.urls import path

from .views import UserRegistrationView, TokenPairObtainView, RefreshTokenObtainView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('token/', TokenPairObtainView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', RefreshTokenObtainView.as_view(), name='token-refresh'),
]