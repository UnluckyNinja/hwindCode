from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'container', 'key']
    
    search_fields = ['name', 'container']