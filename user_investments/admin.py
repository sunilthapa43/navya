from django.contrib import admin

from user_investments.models import UserInvestments

# Register your models here.
admin.site.register(
    UserInvestments,
    list_display=["mutual_fund", "units", "user"],
    list_filter=["mutual_fund", "user"],
)
