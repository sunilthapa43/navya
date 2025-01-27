from django.urls import path

from user_investments.views import UserInvestmentView

urlpatterns = [
    path("", UserInvestmentView.as_view(), name="user_investments"),
    path("<int:pk>/", UserInvestmentView.as_view(), name="user_investment"),
]
