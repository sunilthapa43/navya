from rest_framework import status

from core.views import NavyaAuthView, ErrorResponse, SuccessResponse
from mutual_funds.models import MutualFund
from mutual_funds.serializers import MutualFundSerializer


# Create your views here.


class MutualFundView(NavyaAuthView):
    serializer_class = MutualFundSerializer
    queryset = MutualFund.objects.all()

    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return ErrorResponse(
                success=False,
                error="You are not authorized to perform this action",
                status=status.HTTP_401_UNAUTHORIZED
            )
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return ErrorResponse(
                success=False,
                error=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return SuccessResponse(
            success=True,
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )

    def get(self, request, *args, **kwargs):
        query_set = self.get_queryset()
        if self.request.query_params.get("id"):
            query_set = query_set.filter(id=self.request.query_params.get("id"))
        serializer = self.get_serializer(query_set, many=True)
        return SuccessResponse(
            success=True,
            data=serializer.data,
            status=status.HTTP_200_OK
        )