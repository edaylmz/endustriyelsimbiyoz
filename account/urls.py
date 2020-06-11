from django.contrib import admin

from django.conf.urls import include, url
from .views import *


urlpatterns = [

    url(r'^kayitol/$', account_kayitol,name="kayitol"),
    url(r'^giris/$', account_giris,name="giris"),
    url(r'^cikis/$', account_cikis,name="cikis"),
    url(r'^$',account_anasayfa,name="anasayfa"),
    # url(r'^(?P<id>/d+/$',account_profil,name='profil'),

]
