from decimal import Decimal

from rest_framework import serializers


class UserReportSerializer(serializers.Serializer):
    mutual_fund = serializers.CharField(source='mutual_fund__name')
    nav= serializers.DecimalField(source='mutual_fund__nav', max_digits=12, decimal_places=4)
    total_units = serializers.DecimalField(source='sum_units', max_digits=12, decimal_places=4)
    total_value = serializers.DecimalField(max_digits=12, decimal_places=4, read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        total_units = representation.get('total_units', 0)
        nav= representation.get('nav', 0)

        # Calculate total_value: total_units * mutual_fund_nav
        total_value = Decimal(total_units) * Decimal(nav)
        representation['total_value'] = total_value

        return representation