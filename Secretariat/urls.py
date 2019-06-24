from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

import settings
from django.views.static import serve
from .views import home
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from settings import os


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'acceuil', home.as_view(), name='acceuil'),
    url(r'^media/(?P<path>.*)',serve, {'document_root':settings.MEDIA_ROOT},name='img')
    #url(r'^images/([^/]*)/(\d*)/([^/]*)/[^/]*$', ServeView.as_view(), name='wagtailimages_serve'),
   # url(r'', include(wagtail_urls)),

    # url('^admin/logout',logout,{'next_page':'acceuil'},name='logout')
]


if settings.DEBUG:
    # urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='img')]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

