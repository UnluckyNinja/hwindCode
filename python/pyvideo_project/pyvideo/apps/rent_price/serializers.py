from rest_framework import serializers
from . import models

class RentPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RentPrice
        fields = ('date_value', 'bed_bath', 'model_name', 'room_no', 'available_date', 'price', 'sqft', 'timestamp')