import requests
from rest_framework import status

from core.views import ErrorResponse, NavyaAuthView, SuccessResponse
from mutual_funds.models import MutualFund
from mutual_funds.serializers import MutualFundSerializer


# Create your views here.
def get_ip_location(ip):
    # Make a request to the ipinfo.io API
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()

    # Extract location info
    location = {
        "ip": data.get("ip"),
        "city": data.get("city"),
        "region": data.get("region"),
        "country": data.get("country"),
        "location": data.get("loc"),
        "org": data.get("org"),
    }

    return location


class MutualFundView(NavyaAuthView):
    serializer_class = MutualFundSerializer
    queryset = MutualFund.objects.all()

    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return ErrorResponse(
                success=False,
                error="You are not authorized to perform this action",
                status=status.HTTP_401_UNAUTHORIZED,
            )
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return ErrorResponse(
                success=False, error=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return SuccessResponse(
            success=True, data=serializer.data, status=status.HTTP_201_CREATED
        )

    def get(self, request, *args, **kwargs):
        query_set = self.get_queryset()
        pk = kwargs.get("pk")
        if pk:
            query_set = query_set.filter(id=pk)
        serializer = self.get_serializer(query_set, many=True)
        print("Checking IP Address of the user")
        # get location from Ip address
        ip = request.META.get(
            "HTTP_X_FORWARDED_FOR", request.META.get("REMOTE_ADDR", "")
        ).split(",")[0]
        if ip == "127.0.0.1":
            ip = "2400:1a00:b040:15ca:dff:8b92:5514:ffe"
        print("Full location info is: ", get_ip_location(ip))
        return SuccessResponse(
            success=True, data=serializer.data, status=status.HTTP_200_OK
        )
