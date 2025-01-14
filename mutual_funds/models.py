from django.db import models


# Create your models here.
class MutualFund(models.Model):
    name = models.CharField(max_length=100)
    # create textchoices class for fund type
    class FundType(models.TextChoices):
        EQUITY = "Equity", "Equity"
        DEBT = "Debt", "Debt"
        HYBRID = "Hybrid", "Hybrid"
    symbol = models.CharField(max_length=10)
    fund_type = models.CharField(max_length=10, choices=FundType.choices)
    nav = models.DecimalField(max_digits=12, decimal_places=4)

