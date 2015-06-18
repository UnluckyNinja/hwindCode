# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='id',
            field=models.CharField(unique=True, verbose_name='id', serialize=False, primary_key=True, editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='storage',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
    ]
