from django.urls import path

from reports.views import ReportView

urlpatterns = [
    path("", ReportView.as_view(), name="report"),
]