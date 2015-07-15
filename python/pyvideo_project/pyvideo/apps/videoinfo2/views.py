import uuid
import random
import os
from collections import OrderedDict
from . import models
from .models import Storage, Video, VideoFile
from . import serializers
from .serializers import StorageSerializer, VideoSerializer, VideoFileSerializer, VideoDetailSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

Chunck_Size = 20 * 1024 * 1024

def estimate_chuncks(size):
    if size % Chunck_Size == 0:
        return size // Chunck_Size
    else:
        return size // Chunck_Size + 1

class StorageList(APIView):
    def get(self, request, format=None):
        storages = Storage.objects.all()
        serializer = StorageSerializer(storages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StorageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_404_BAD_REQUEST)

class StorageDetail(APIView):
    def get_object(self, pk):
        try:
            return Storage.objects.get(id=pk)
        except Storage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        storage = self.get_object(pk)
        serializer = StorageSerializer(storage)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        storage = self.get_object(pk)
        serializer = StorageSerializer(storage, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_404_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        storage = self.get_object(pk)
        storage.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class VideoList(APIView):
    def get(self, request, format=None):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if 'SSL_CLIENT_I_DN_CN' in os.environ:
            cn = os.environ['SSL_CLIENT_I_DN_CN']
            if cn == 'dev at hwind-linux':
                user = 2
            else:
                user = 1
        else:
            user = 3

        request.data['user'] = user
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            chuncks = estimate_chuncks(serializer.instance.size)
            storages = Storage.objects.all()
            for i in range(0, chuncks):
                vf = VideoFile()
                vf.videoid = serializer.instance
                vf.path = uuid.uuid4().hex
                rd = random.randint(0, len(storages)-1)
                vf.storageid = storages[rd]
                vf.index = i
                vf.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class VideoDetail(APIView):
    def get_object(self, pk):
        try:
            return Video.objects.get(id=pk)
        except Video.DoesNotExist:
            raise Http404

    def get_vf_object(self, pk):
        try:
            return VideoFile.objects.filter(videoid__exact=pk)
        except VideoFile.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        video = self.get_object(pk)
        vfs = self.get_vf_object(pk)
        data = OrderedDict({'video': VideoSerializer(video).data})
        data['video_files'] = VideoFileSerializer(vfs, many=True).data
        #data = OrderedDict({'video': VideoSerializer(video).data, 'video_files': VideoFileSerializer(vfs, many=True).data})
        #serializer = VideoDetailSerializer(data)
        #serializer.is_valid(raise_exception=True)
        return Response(data)

    def delete(self, request, pk, format=None):
        video = self.get_object(pk)
        vfs = self.get_vf_object(pk)

        if vfs != None:
            vfs.delete()
        if video != None:
            video.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)