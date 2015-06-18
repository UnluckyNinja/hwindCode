# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('videoinfo', '0003_video_videofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='create_time',
            field=models.DateTimeField(verbose_name='create_time', auto_now_add=True, default=datetime.datetime(2015, 6, 17, 21, 47, 33, 519591, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='update_time',
            field=models.DateTimeField(verbose_name='update_time', default=datetime.datetime(2015, 6, 17, 21, 48, 0, 834525, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
