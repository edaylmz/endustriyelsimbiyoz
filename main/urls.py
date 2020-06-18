from django.contrib import admin

from django.conf.urls import include, url
from django.urls import path

from main import views
from .views import *

urlpatterns = [

    url(r'^AtikEkle/$', views.AtikCreate.as_view(), name="AtikEkle"),
    url(r'^AtikUpdate/(?P<pk>[0-9]+)/$', views.AtikUpdate.as_view(), name="atikupdate"),
    url(r'^HammaddeUpdate/(?P<pk>[0-9]+)/$', views.HammaddeUpdate.as_view(), name="hammaddeupdate"),
    url(r'^HammaddeEkle/$', views.HammaddeCreate.as_view(), name="HammaddeEkle"),
    url(r'^UreticiBilgileri/$', main_UreticiBilgileri, name="UreticiBilgileri"),
    url(r'^profil/$', main_profil, name="profil"),
    url(r'^firmaupdate/$', firma_update, name="firmaupdate"),
    url(r'^firmagoruntule/', firma_show, name="firmagoruntule"),
    url(r'^firmagor/(?P<id>[0-9]+)/$', firma_gor, name="firmagor"),
    url(r'^profiltuketici/$', profil_tuketici, name="profiltuketici"),
    url(r'^atikgor/(?P<id>[0-9]+)/$', atik_show, name="atikgoruntule"),
    url(r'^atikara/$',atik_ara,name="atik_ara"),
    url(r'^hammaddeara/$',hammadde_ara,name="hammadde_ara"),
    url(r'^atikdelete/(?P<id>[0-9]+)/$', atik_sil, name="atiksil"),
    url(r'^hammaddegor/(?P<id>[0-9]+)/$', hammadde_show, name="hammaddegor"),
    url(r'^hammaddedelete/(?P<id>[0-9]+)/$', hammadde_sil, name="hammaddesil"),

]
