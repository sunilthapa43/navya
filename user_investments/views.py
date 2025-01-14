from rest_framework import status
from core.views import NavyaAuthView, ErrorResponse, SuccessResponse, NavyaSuperUserView
from user_investments.models import UserInvestments
from user_investments.serializers import UserInvestmentsSerializer
# Create your views here.



class UserInvestmentView(NavyaAuthView):
    queryset = UserInvestments.objects.all()
    serializer_class = UserInvestmentsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return ErrorResponse(
                success=False,
                error=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(
            user=request.user
        )
        return SuccessResponse(
            success=True,
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )

    def get(self, request, *args, **kwargs):
        query_set = self.query_set.filter(user=request.user)
        if self.request.query_params.get("id"):
            query_set = query_set.filter(id=self.request.query_params.get("id"))
        serializer = self.get_serializer(query_set, many=True)
        return SuccessResponse(
            success=True,
            data=serializer.data,
            status=status.HTTP_200_OK
        )

