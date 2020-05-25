from django.contrib import admin

from django.conf.urls import include,url
from .views import *

urlpatterns = [

    url(r'^AtikEkle/$',main_AtikEkle),
    url(r'^AtikBilgileri/$',main_AtikBilgileri),
    url(r'^UreticiBilgileri/$',main_UreticiBilgileri),
    url(r'^profil/$', main_profil),
    url(r'^BilesenAnaliz/$', main_BilesenAnaliz),


    url(r'^yazdir/([\w\-]+)/$', sayfayiyazdir, name='sayfayiyazdir'),


]