from django.db import models


# Create your models here.
class MutualFund(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # create textchoices class for fund type
    class FundType(models.TextChoices):
        EQUITY = "Equity", "Equity"
        DEBT = "Debt", "Debt"
        HYBRID = "Hybrid", "Hybrid"
    symbol = models.CharField(max_length=10, unique=True)
    fund_type = models.CharField(max_length=10, choices=FundType.choices)
    nav = models.DecimalField(max_digits=12, decimal_places=4)

    def __str__(self):
        return f"{self.name} - {self.symbol}"

    class Meta:
        verbose_name_plural = "Mutual Funds"
        unique_together = ['name', 'symbol']

