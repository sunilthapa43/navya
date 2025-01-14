from rest_framework import serializers

from mutual_funds.models import MutualFund


class MutualFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = MutualFund
        fields = '__all__'
