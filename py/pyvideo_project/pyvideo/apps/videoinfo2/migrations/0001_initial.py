# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.CharField(serialize=False, max_length=100, verbose_name='id', primary_key=True, editable=False, unique=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('container', models.CharField(max_length=100, verbose_name='container')),
                ('key', models.CharField(max_length=300, verbose_name='key')),
            ],
            options={
                'verbose_name_plural': 'Storages',
                'verbose_name': 'Storage',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.CharField(serialize=False, max_length=100, verbose_name='id', primary_key=True, editable=False, unique=True)),
                ('name', models.CharField(max_length=2000, verbose_name='name')),
                ('size', models.BigIntegerField(verbose_name='size')),
                ('md5', models.CharField(max_length=100, verbose_name='md5')),
                ('state', models.IntegerField(verbose_name='state')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='videos2', verbose_name='user')),
            ],
            options={
                'verbose_name_plural': 'Videos',
                'verbose_name': 'Video',
            },
        ),
        migrations.CreateModel(
            name='VideoFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('path', models.CharField(max_length=2000, verbose_name='path')),
                ('index', models.PositiveIntegerField(verbose_name='index')),
                ('storageid', models.ForeignKey(to='videoinfo2.Storage', related_name='videofiles', verbose_name='storageid')),
                ('videoid', models.ForeignKey(to='videoinfo2.Video', related_name='videofiles', verbose_name='videoid')),
            ],
            options={
                'verbose_name_plural': 'VideoFiles',
                'verbose_name': 'VideoFile',
            },
        ),
    ]
