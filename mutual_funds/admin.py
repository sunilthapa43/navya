from django.contrib import admin

from mutual_funds.models import MutualFund

# Register your models here.

admin.site.register(
    MutualFund,
    list_display=['name', 'symbol', 'nav', 'fund_type', 'id'],
    list_filter=['name', 'symbol']
)