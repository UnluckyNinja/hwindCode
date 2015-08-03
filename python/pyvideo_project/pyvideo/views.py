# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import os
import pdb
from .apps.videoinfo2 import models as videoinfo2_model
 
def home(request):
    if request.user.is_authenticated():
        videos = videoinfo2_model.Video.objects.filter(user = request.user.id)
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
        v = videoinfo2_model.Video(user = request.user, name = fname, size = size, md5 = md5, state = 0)
        v.save()
        return HttpResponseRedirect(reverse("home"))

def delete_video(request):
    to_delete_ids = request.POST.getlist('video_check')
    for item in to_delete_ids:
        v = videoinfo2_model.Video.objects.filter(id = item)
        v.delete()
    return HttpResponseRedirect(reverse("home"))

def search_video(request):
    search_content = request.GET["search_input"]
    videos = videoinfo2_model.Video.objects.filter(name__icontains = search_content)
    return render(request, "videoinfo.html", {'videos': videos, 'tmpuser':request.user})