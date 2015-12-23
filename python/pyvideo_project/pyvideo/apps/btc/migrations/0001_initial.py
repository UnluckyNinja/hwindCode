# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BTCTrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('timestamp', models.DateTimeField(unique=True, verbose_name='timestamp', auto_now_add=True)),
                ('btcc_btc_free', models.FloatField(verbose_name='btcc_btc_free')),
                ('btcc_btc_frozen', models.FloatField(verbose_name='btcc_btc_frozen')),
                ('btcc_cny_free', models.FloatField(verbose_name='btcc_cny_free')),
                ('btcc_cny_frozen', models.FloatField(verbose_name='btcc_cny_frozen')),
                ('btcc_price', models.FloatField(verbose_name='btcc_price')),
                ('ok_btc_free', models.FloatField(verbose_name='ok_btc_free')),
                ('ok_btc_frozen', models.FloatField(verbose_name='ok_btc_frozen')),
                ('ok_cny_free', models.FloatField(verbose_name='ok_cny_free')),
                ('ok_cny_frozen', models.FloatField(verbose_name='ok_cny_frozen')),
                ('ok_price', models.FloatField(verbose_name='ok_price')),
            ],
            options={
                'verbose_name_plural': 'BTCTrade',
                'verbose_name': 'BTCTrade',
            },
        ),
    ]
