from decimal import Decimal

from rest_framework import serializers
from user_investments.models import UserInvestments


class UserReportSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()
    nav = serializers.SerializerMethodField()

    def get_value(self, obj):
        return Decimal(obj.units) * Decimal(obj.mutual_fund.nav)

    def get_nav(self, obj):
        return obj.mutual_fund.nav

    def to_representation(self, instance):
        # Get the original representation
        representation = super().to_representation(instance)

        # Replace the mutual_fund field with its name
        representation['mutual_fund'] = instance.mutual_fund.name  # Assuming 'name' is the field in mutual_fund

        return representation

    class Meta:
        model = UserInvestments
        fields = [
            'mutual_fund',
            'units',
            "nav",
            'value'
        ]
