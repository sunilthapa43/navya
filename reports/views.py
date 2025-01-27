from django.db.models import Sum
from rest_framework import status

from core.views import NavyaAuthView, SuccessResponse
from reports.serializers import UserReportSerializer
from user_investments.models import UserInvestments


class ReportView(NavyaAuthView):
    serializer_class = UserReportSerializer

    def get(self, request, *args, **kwargs):
        investments = (
            UserInvestments.objects.filter(user=request.user)
            .select_related("mutual_fund")
            .values(
                "mutual_fund__name",
                "mutual_fund__nav",
            )
            .annotate(
                sum_units=Sum("units"),
            )
        )
        serializer = self.get_serializer(investments, many=True)
        return SuccessResponse(
            success=True,
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
