from rest_framework import serializers
from . import models

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Storage
        fields = ('id', 'name', 'container', 'key')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = ('user', 'id', 'name', 'size', 'md5', 'state', 'create_time', 'update_time')

class VideoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VideoFile
        fields = ('videoid', 'storageid', 'path', 'index')
            