from django.contrib.auth.models import User
from rest_framework import status

from core.views import NavyaSuperUserView, SuccessResponse, NavyaAuthView
from reports.serializers import UserReportSerializer
from user_investments.models import UserInvestments


class ReportView(NavyaAuthView):
    serializer_class = UserReportSerializer

    def get(self, request, *args, **kwargs):
        investments = UserInvestments.objects.filter(user=request.user)
        if self.request.query_params.get("id"):
            investments = investments.filter(id=self.request.query_params.get("id"))
        serializer = self.get_serializer(investments, many=True)
        return SuccessResponse(
            success=True,
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

