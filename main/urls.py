from django.contrib import admin

from django.conf.urls import include, url
from django.urls import path

from main import views
from .views import *

urlpatterns = [

    url(r'^AtikEkle/$', views.AtikCreate.as_view(), name="AtikEkle"),
    url(r'^HammaddeEkle/$', views.HammaddeCreate.as_view(), name="HammaddeEkle"),
    url(r'^UreticiBilgileri/$', main_UreticiBilgileri, name="UreticiBilgileri"),
    url(r'^profil/$', main_profil, name="profil"),
    url(r'^firmaupdate/$', firma_update, name="firmaupdate"),
    url(r'^firmagoruntule/$', firma_show, name="firmagoruntule"),
    url(r'^profiltuketici/$', profil_tuketici, name="profiltuketici"),
    url(r'^atikgor/(?P<id>[0-9]+)/$', atik_show, name="atikgoruntule")

]
