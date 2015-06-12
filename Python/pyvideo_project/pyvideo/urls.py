from django.conf.urls import include, url
from django.contrib import admin
from .views import home

urlpatterns = [
    # Examples:
    # url(r'^$', 'pyvideo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', home, name='home'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
]
