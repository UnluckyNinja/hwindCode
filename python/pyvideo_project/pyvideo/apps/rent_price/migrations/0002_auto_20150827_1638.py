# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent_price', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentprice',
            name='date_value',
            field=models.DateField(verbose_name='date_value'),
        ),
    ]
