# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('btc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='btctrade',
            name='src',
            field=models.CharField(max_length=10, default='aliyun_1'),
        ),
    ]
