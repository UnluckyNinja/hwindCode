# -*- coding: utf-8 -*-
import uuid
from django.db import models
from django.conf import settings

from . import managers
# Create your models here.

class Storage(models.Model):
    # Relations
    
    #Attributes
    id = models.CharField(
        max_length = 100,
        null = False,
        blank = False,
        unique = True,
        primary_key = True,
        editable = False,
        verbose_name = 'id'
        )
    
    name = models.CharField(
        max_length = 100,
        null = False,
        blank = False,
        unique = False,
        verbose_name = 'name'
        )
    
    container = models.CharField(
        max_length = 100,
        null = False,
        blank = False,
        unique = False,
        verbose_name = 'container'
        )
    
    key = models.CharField(
        max_length = 300,
        null = False,
        blank = False,
        unique = False,
        verbose_name = 'key'
        )
    
    #Object Manager
    objects = managers.StorageManager()
    
    #Meta
    class Meta:
        verbose_name = 'Storage'
        verbose_name_plural = 'Storages'
    
    def save(self, *args, **kwargs):
        if not self.pk:  # object is being created, thus no primary key field yet
            self.id = uuid.uuid4().hex
        super(Storage, self).save(*args, **kwargs)
    
    def __str__(self):
        return str.format('{0}@{1}.blob.core.windows.net', self.container, self.name)

class Video(models.Model):
    #Relations
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name = 'videos',
        verbose_name = 'user'
        )
    
    #Attributes
    id = models.CharField(
        max_length = 100,
        null = False,
        blank = False,
        unique = True,
        primary_key = True,
        editable = False,
        verbose_name = 'id'
        )
    
    name = models.CharField(
        max_length = 2000,
        null = False,
        blank = False,
        unique = False,
        verbose_name = 'name'
        )
    
    size = models.BigIntegerField(
        null = False,
        blank = False,
        verbose_name = 'size'
        )
    
    md5 = models.CharField(
        max_length = 100,
        null = False,
        blank = False,
        unique = False,
        verbose_name = 'md5'
        )
    
    state = models.IntegerField(
        null = False,
        verbose_name = 'state'
        )

    create_time = models.DateTimeField(
        auto_now = False,
        auto_now_add = True,
        verbose_name = "create_time"
        )

    update_time = models.DateTimeField(
        auto_now = True,
        auto_now_add = False,
        verbose_name = "update_time"
        )
    
    #Object Manager
    objects = managers.VideoManager()
    
    #Meta
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
    
    def save(self, *args, **kwargs):
        if not self.pk:  # object is being created, thus no primary key field yet
            self.id = uuid.uuid4().hex
        super(Video, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class VideoFile(models.Model):
    #Relations
    videoid = models.ForeignKey(
        Video,
        related_name = 'videofiles',
        verbose_name = 'videoid'
        )
    
    storageid = models.ForeignKey(
        Storage,
        related_name = 'videofiles',
        verbose_name = 'storageid'
        )
    
    #Attributes
    path = models.CharField(
        max_length = 2000,
        null = False,
        blank = False,
        unique = False,
        verbose_name = 'path'
        )
    
    index = models.PositiveIntegerField(
        null = False,
        verbose_name = 'index'
        )

    #Object Manager
    objects = managers.VideoFileManager()
    
    #Meta
    class Meta:
        verbose_name = 'VideoFile'
        verbose_name_plural = 'VideoFiles'