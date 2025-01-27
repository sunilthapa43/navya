from django.urls import path

from mutual_funds.views import MutualFundView

urlpatterns = [
    path("", MutualFundView.as_view(), name="mutual_funds"),
    path("<int:pk>/", MutualFundView.as_view(), name="mutual_fund"),
]
