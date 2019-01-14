"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
# from django.contrib import admin
from app01.views import *

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^my_day/([0-9]{4})/$', my_day),
    # url(r'^my_day/([0-9]{4})/([0-9]{2})/$', my_day2),
    # url(r'^my_day/([0-9]{4})/([0-9]{2})/([0-9]{2})/$', my_day3),
    url(r'^my_day/(?P<year>[0-9]{4})/$', my_day4),
    url(r'^my_day/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', my_day2),
    url(r'^my_day/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', my_day3),
    url(r'^hello', my_hello, name='little_hello'),

]

