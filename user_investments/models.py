from django.db import models

# Create your models here.
# Create a model for user investments with the following fields:
# - id: Auto-generated primary key.
# - user: ForeignKey to the authenticated user.
# - mutual_fund: ForeignKey to mutual funds.
# - units: Number of units (float).

class UserInvestments(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    mutual_fund = models.ForeignKey('mutual_funds.MutualFund', on_delete=models.CASCADE)
    units = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.mutual_fund.name} - {self.units}"

    class Meta:
        verbose_name_plural = "User Investments"