from rest_framework import serializers
from user_investments.models import UserInvestments


class UserInvestmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInvestments
        fields = [
            'id',
            'mutual_fund',
            'units',
        ]
        extra_kwargs = {
            'mutual_fund': {'required': True},
            'units': {'required': True},
            'id': {'read_only': True}
        }

