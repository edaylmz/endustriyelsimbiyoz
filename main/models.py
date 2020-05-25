from __future__ import unicode_literals

from django.db.models import CASCADE
from django.utils import timezone
from django.db import models
from location_field.models.plain import PlainLocationField
from account.models import Uye


# Create your models here.

class FirmaBilgileri(models.Model):
    Firmauye = models.ForeignKey('auth.User', on_delete=CASCADE)
    #FirmaId=models.AutoField(primary_key=True)
    Durum = models.BooleanField(u'Durum')
    FirmaUnvani = models.CharField(u'Firma Ünvanı', max_length=50)
    NACE = models.CharField(u'NACE Kodu', max_length=8)
    FaaliyetAlani = models.TextField(u'Faaliyet Alanı', blank=True)
    Adres = models.CharField(u'Firma Adresi', max_length=300, blank=True)
    Il = models.CharField(u'İl', max_length=30)
    Ilce = models.CharField(u'İlçe', max_length=30, blank=True)
    FirmaTel = models.IntegerField(u'Firma Tel', blank=True)
    Email = models.EmailField(u'Firma Email', blank=True)
    WebSitesi = models.CharField(u'Firma Web Sitesi', max_length=100, blank=True)
    IlgiliAd = models.CharField(u'İlgili Kişi Adı', max_length=50, blank=True)
    IlgiliTel = models.IntegerField(u'İlgili Kişi Tel', blank=True)
    IlgiliEmail = models.EmailField(u'İlgili Kişi Email', blank=True)
    Konum = PlainLocationField(based_fields=['Il'], zoom=7)

    def __unicode__(self):
        return self.FirmaUnvani, self.NACE

    class Meta:
        verbose_name = u"Firma Bilgileri"
        verbose_name_plural = u"Firmalar"


class AtikTemel(models.Model):
    #firma = models.ForeignKey('FirmaBilgileri', on_delete=CASCADE)
    #AtikId=models.AutoField(primary_key=True)
    AtikKodu = models.CharField(u'Atık Kodu', max_length=40)
    FizikselOzellik = models.TextField(u'Fiziksel Özellikleri')
    Renk = models.CharField(u'Renk', max_length=20, blank=True)
    TehlikeOzellik = models.TextField(u'Tehlike Özellikleri', blank=True)
    ProsesBilgi = models.TextField(u'Proses Bilgileri', blank=True)
    AtikAnaliz = models.TextField(u'Atık Analizleri', blank=True)
    Miktar = models.CharField(u'Yıllık Atık Miktarı', max_length=400)
    TasimaOnlem = models.TextField(u'Taşıma Önlemleri', blank=True)
    Notlar = models.TextField(u'Notlar', blank=True)
    Dosyalar = models.FileField(u'Dosyalar', blank=True)

    def __unicode__(self):
        return self.AtikKodu

    class Meta:
        verbose_name_plural = u"Atıklar"
        verbose_name = u"Atık"


class BilesenAnaliz(models.Model):
    #AtikKodu = models.ForeignKey('AtikTemel', on_delete=CASCADE
    #BilesenId=models.AutoField(primary_key=True)
    AtikTanim = models.TextField(u'Atık Tanımı')
    TicariAdi = models.CharField(u'Atığın Ticari Adı', max_length=40)
    Synonim1 = models.CharField(u'Sinonim1', max_length=40)
    Synonim2 = models.CharField(u'Sinonim2', max_length=40)
    ProsesAmac = models.TextField(u'Prosesin Amacı')
    ProsesAsama = models.CharField(u'Atığın Kaynaklandığı Proses Aşaması', max_length=50)
    ProsesOzet = models.TextField(u'Proses Özeti')
    EK3B = models.FileField(u'Ek3-B Analizi')
    EK2 = models.FileField(u'EK-2 Analizi')

    def __unicode__(self):
        return self.TicariAdi,self.AtikKodu

    class Meta:
        verbose_name_plural=u"Bilesenler"
        verbose_name=u"Bilesen"