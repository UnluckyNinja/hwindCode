# -*- coding: utf-8 -*-
import uuid
from django.db import models
from django.conf import settings

from . import managers
# Create your models here.

class BTCTrade(models.Model):
    timestamp = models.DateTimeField(
        auto_now = False,
        auto_now_add = True,
        verbose_name = "timestamp",
        unique = True
        )

    btcc_btc_free = models.FloatField(
        verbose_name = "btcc_btc_free"
        )

    btcc_btc_frozen = models.FloatField(
        verbose_name = "btcc_btc_frozen"
        )

    btcc_cny_free = models.FloatField(
        verbose_name = "btcc_cny_free"
        )

    btcc_cny_frozen = models.FloatField(
        verbose_name = "btcc_cny_frozen"
        )

    btcc_price = models.FloatField(
        verbose_name = "btcc_price"
        )

    ok_btc_free = models.FloatField(
        verbose_name = "ok_btc_free"
        )

    ok_btc_frozen = models.FloatField(
        verbose_name = "ok_btc_frozen"
        )

    ok_cny_free = models.FloatField(
        verbose_name = "ok_cny_free"
        )

    ok_cny_frozen = models.FloatField(
        verbose_name = "ok_cny_frozen"
        )

    ok_price = models.FloatField(
        verbose_name = "ok_price"
        )

    #Object
    objects = managers.BTCTradeManager()

    #Meta
    class Meta:
        verbose_name = 'BTCTrade'
        verbose_name_plural = 'BTCTrade'