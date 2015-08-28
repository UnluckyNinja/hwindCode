from django.conf.urls import include, url
from django.contrib import admin
from .views import *
from pyvideo.apps import videoinfo2
from pyvideo.apps.videoinfo2 import urls
from pyvideo.apps import rent_price
from pyvideo.apps.rent_price import urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'pyvideo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest/', include(videoinfo2.urls)),
    url(r'^rent/', include(rent_price.urls)),
	url(r'^$', home, name='home'),
    url(r'^delete_video', delete_video, name='delete_video'),
    url(r'^search_video', search_video, name='search_video'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
]