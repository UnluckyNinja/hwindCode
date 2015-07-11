# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.CharField(verbose_name='id', primary_key=True, serialize=False, unique=True, max_length=100)),
                ('name', models.CharField(unique=True, verbose_name='name', max_length=100)),
                ('container', models.CharField(verbose_name='container', max_length=100)),
                ('key', models.CharField(verbose_name='key', max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Storages',
                'verbose_name': 'Storage',
            },
        ),
    ]
