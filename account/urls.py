from django.contrib import admin

from django.conf.urls import include, url
from .views import *

urlpatterns = [

    url(r'^kayitol/$', account_kayitol),
    url(r'^giris/$', account_giris),
    url(r'^cikis/$', account_cikis),
    url(r'^$',account_anasayfa),
    # url(r'^(?P<id>/d+/$',account_profil,name='profil'),

]
