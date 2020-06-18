from __future__ import unicode_literals

from django import conf

from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import CASCADE

from django.db import models

# Create your models here.
from location_field import settings


class FirmaBilgileri(models.Model):
    Firmauye = models.ForeignKey(User, on_delete=CASCADE)
    # FirmaId=models.AutoField(primary_key=True)
    # Durum = models.BooleanField(u'Durum')
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

    # Konum = PlainLocationField(based_fields=['Il'], zoom=7)

    def __unicode__(self):
        return self.FirmaUnvani, self.NACE

    class Meta:
        verbose_name = u"Firma Bilgileri"
        verbose_name_plural = u"Firmalar"


class AtikTemel(models.Model):
    firma = models.ForeignKey('auth.User', on_delete=CASCADE,null=True)
    # AtikId=models.AutoField(primary_key=True)
    Il = models.CharField(u'İl', max_length=50,null=True)
    Ilce = models.CharField(u'İlce', max_length=50,null=True)
    AtikKodu = models.CharField(u'Atık Kodu', max_length=40)
    FizikselOzellik = models.CharField(u'Fiziksel Özellikleri', max_length=500)
    Renk = models.CharField(u'Renk', max_length=20, blank=True, null=True)
    TehlikeOzellik = models.CharField(u'Tehlike Özellikleri', max_length=500, blank=True, null=True)
    ProsesBilgi = models.CharField(u'Proses Bilgileri', max_length=500, blank=True, null=True)
    AtikAnaliz = models.CharField(u'Atık Analizleri', max_length=500, blank=True, null=True)
    Miktar = models.CharField(u'Yıllık Atık Miktarı', max_length=400)
    AtikTanim = models.CharField(u'Atık Tanımı', max_length=500)
    TicariAdi = models.CharField(u'Atığın Ticari Adı', max_length=40)
    ProsesAmac = models.CharField(u'Prosesin Amacı', max_length=500)
    ProsesAsama = models.CharField(u'Atığın Kaynaklandığı Proses Aşaması', max_length=50)
    ProsesOzet = models.CharField(u'Proses Özeti', max_length=500)
    EK3B = models.FileField(u'Ek3-B Analizi', blank=True, null=True)
    EK2 = models.FileField(u'EK-2 Analizi', blank=True, null=True)

    def __unicode__(self):
        return self.AtikKodu

    class Meta:
        verbose_name = u"Atık"
        verbose_name_plural = u"Atıklar"


class Bilesenler(models.Model):
    atik = models.ForeignKey(AtikTemel, on_delete=CASCADE, related_name="atık")
    Bilesenadi = models.CharField(u'Bileşen Adı', max_length=20)
    max = models.IntegerField(u'Max')
    min = models.IntegerField(u'Min')
    yuzde = models.IntegerField(u'Yüzde')

    def __unicode__(self):
        return self.Bilesenadi

    class Meta:
        verbose_name = u"Atık Bilesen"
        verbose_name_plural = u"Atık Bilesenler"


class Hammadde(models.Model):
    firma = models.ForeignKey('auth.User', on_delete=CASCADE,null=True)
    Il = models.CharField(u'İl', max_length=50, null=True)
    Ilce = models.CharField(u'İlçe', max_length=50, null=True)
    TicariAdi = models.CharField(u'Ticari Adı', max_length=100)
    Miktar = models.IntegerField(u'Yıllık Miktarı')

    def __unicode__(self):
        return self.TicariAdi

    class Meta:
        verbose_name_plural = u"Hammaddeler"
        verbose_name = u"Hammadde"


class HammaddeBilesenler(models.Model):
    # uye = models.ForeignKey('auth.User', on_delete=CASCADE)
    hammadde = models.ForeignKey(Hammadde, on_delete=CASCADE, related_name="atık")
    Bilesenadi = models.CharField(u'Bileşen Adı', max_length=20)
    max = models.IntegerField(u'Max')
    min = models.IntegerField(u'Min')
    yuzde = models.IntegerField(u'Yüzde')

    def __unicode__(self):
        return self.Bilesenadi

    class Meta:
        verbose_name = u"Bilesen"
        verbose_name_plural = u"Bilesenler"
