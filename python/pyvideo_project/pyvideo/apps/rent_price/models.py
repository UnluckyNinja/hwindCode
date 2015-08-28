# -*- coding: utf-8 -*-
import uuid
from django.db import models
from django.conf import settings

from . import managers
# Create your models here.

class RentPrice(models.Model):
    date_value = models.DateField(
        verbose_name = 'date_value'
        )

    bed_bath = models.CharField(
        max_length = 20,
        null = False,
        blank = False,
        unique = False,
        verbose_name = 'bed_bath'
        )

    model_name = models.CharField(
        max_length = 20,
        null = False,
        blank = False,
        unique = False,
        verbose_name = 'model_name'
        )

    room_no = models.CharField(
        max_length = 20,
        null = False,
        blank = False,
        unique = False,
        verbose_name = 'room_no'
        )

    available_date = models.CharField(
        max_length = 20,
        null = False,
        blank = False,
        unique = False,
        verbose_name = 'available_date'
        )

    price = models.IntegerField(
        null = False,
        verbose_name = 'price'
        )

    sqft = models.IntegerField(
        null = False,
        verbose_name = 'sqft'
        )

    timestamp = models.DateTimeField(
        auto_now = False,
        auto_now_add = True,
        verbose_name = "timestamp"
        )

    #Object
    objects = managers.RentPriceManager()

    #Meta
    class Meta:
        verbose_name = 'RentPrice'
        verbose_name_plural = 'RentPrice'
        unique_together = ('date_value', 'room_no')