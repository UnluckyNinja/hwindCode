# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RentPrice',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date_value', models.DateTimeField(verbose_name='date_value')),
                ('bed_bath', models.CharField(max_length=20, verbose_name='bed_bath')),
                ('model_name', models.CharField(max_length=20, verbose_name='model_name')),
                ('room_no', models.CharField(max_length=20, verbose_name='room_no')),
                ('available_date', models.CharField(max_length=20, verbose_name='available_date')),
                ('price', models.IntegerField(verbose_name='price')),
                ('sqft', models.IntegerField(verbose_name='sqft')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
            ],
            options={
                'verbose_name': 'RentPrice',
                'verbose_name_plural': 'RentPrice',
            },
        ),
        migrations.AlterUniqueTogether(
            name='rentprice',
            unique_together=set([('date_value', 'room_no')]),
        ),
    ]
