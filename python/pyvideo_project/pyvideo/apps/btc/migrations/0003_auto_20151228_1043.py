# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('btc', '0002_btctrade_src'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btctrade',
            name='src',
            field=models.CharField(max_length=20, default='aliyun_1'),
        ),
    ]
