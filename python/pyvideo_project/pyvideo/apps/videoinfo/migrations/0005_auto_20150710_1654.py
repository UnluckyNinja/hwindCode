# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('videoinfo', '0004_auto_20150617_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='videos1', verbose_name='user'),
        ),
    ]
