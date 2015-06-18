# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videoinfo', '0002_auto_20150614_0044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.CharField(verbose_name='id', editable=False, primary_key=True, unique=True, serialize=False, max_length=100)),
                ('name', models.CharField(verbose_name='name', max_length=2000)),
                ('size', models.BigIntegerField(verbose_name='size')),
                ('md5', models.CharField(verbose_name='md5', max_length=100)),
                ('state', models.IntegerField(verbose_name='state')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL, related_name='videos')),
            ],
            options={
                'verbose_name_plural': 'Videos',
                'verbose_name': 'Video',
            },
        ),
        migrations.CreateModel(
            name='VideoFile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('path', models.CharField(verbose_name='path', max_length=2000)),
                ('index', models.PositiveIntegerField(verbose_name='index')),
                ('storageid', models.ForeignKey(verbose_name='storageid', to='videoinfo.Storage', related_name='videofiles')),
                ('videoid', models.ForeignKey(verbose_name='videoid', to='videoinfo.Video', related_name='videofiles')),
            ],
            options={
                'verbose_name_plural': 'VideoFiles',
                'verbose_name': 'VideoFile',
            },
        ),
    ]
