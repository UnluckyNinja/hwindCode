# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from .apps.videoinfo import models as videoinfo_model
 
def home(request):
    if request.user.is_authenticated():
        videos = videoinfo_model.list_videoinfo(request.user.id)
        return render(request, "videoinfo.html", {'videos':videos, 'tmpuser':request.user})

    else:
        return render(request, "index.html", {})

def  add_video(request):
    if request.user.is_authenticated() == False:
        return render(request, "index.html", {})

    if request.method == "GET":
        return render(request, "add_video.html", {})
    elif request.method == "POST":
        fname = request.POST["fname"]
        size = 1023
        md5 = "hello world"
        videoinfo_model.upload_videoinfo(request.user, fname, size, md5)
        return home(request)
