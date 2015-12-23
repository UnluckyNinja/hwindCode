from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.BTCTrade)
class BTCTradeAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'btcc_btc_free', 'btcc_btc_frozen', 'btcc_cny_free', 'btcc_cny_frozen'
        ,'btcc_price', 'ok_btc_free', 'ok_btc_frozen', 'ok_cny_free', 'ok_cny_frozen', 'ok_price']

    search_fields = ['timestamp']