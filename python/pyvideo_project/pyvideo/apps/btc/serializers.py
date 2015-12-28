from rest_framework import serializers
from . import models

class BTCTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BTCTrade
        fields = ('timestamp', 'src', 'btcc_btc_free', 'btcc_btc_frozen', 'btcc_cny_free', 'btcc_cny_frozen'
            ,'btcc_price', 'ok_btc_free', 'ok_btc_frozen', 'ok_cny_free', 'ok_cny_frozen', 'ok_price')