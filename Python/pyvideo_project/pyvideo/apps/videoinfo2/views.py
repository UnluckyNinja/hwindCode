from . import models
from .models import Storage
from . import serializers
from .serializers import StorageSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

