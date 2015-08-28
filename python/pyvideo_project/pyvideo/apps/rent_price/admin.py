from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.RentPrice)
class RentPriceAdmin(admin.ModelAdmin):
    list_display = ['date_value', 'bed_bath', 'model_name', 'room_no', 'available_date', 'price', 'sqft', 'timestamp']

    search_fields = ['date_value', 'bed_bath', 'model_name']