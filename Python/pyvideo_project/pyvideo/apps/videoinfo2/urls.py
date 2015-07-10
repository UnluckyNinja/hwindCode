from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^storage$', views.StorageList.as_view()),
    url(r'^storage/(?P<pk>[^/]+)$', views.StorageDetail.as_view()),
    url(r'^video$', views.VideoList.as_view()),
    url(r'^video/(?P<pk>[^/]+)$', views.VideoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)