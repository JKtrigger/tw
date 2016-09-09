"""tw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
import litleTwit.views
urlpatterns = [
    url(r'^here/', admin.site.urls),
    url(r'^$', litleTwit.views.start,name = 'index'),
    url(r'^login/$', litleTwit.views.login),
    url(r'^logout$', litleTwit.views._logout),
    url(r'^KeepIt/$', litleTwit.views.KeepIt),
    url(r'^refresh/$', litleTwit.views.refresh),
    url(r'^Search/$', litleTwit.views.search),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,}),
]
