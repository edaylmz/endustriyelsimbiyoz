from __future__ import unicode_literals

import random
import string

from django.db import models
from django.utils import timezone


# Create your models here.

class Uye(models.Model):
    ad = models.CharField(u'Ad ', max_length=30)
    soyad = models.CharField(u'Soyad ', max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    kayitTarihi = models.DateField(u"Kayıt Tarihi", default=timezone.now)
    UyeKodu = models.CharField(u'Üye Kodu', default=''.join(random.choice(string.digits) for x in range(8)),
                               max_length=8)

    def __unicode__(self):
        return "Uye Kodu: %s Adı Soyadı: %s %s" % (self.UyeKodu, self.ad, self.soyad)

    class Meta:
        verbose_name_plural = u"Members"
        verbose_name = u"Member"

    def Yazdir(self):
        return '<a href ="/yazdir/%s" target="_blank">Yazdir</a>' % self.id

    Yazdir.short_description = u'Yazdir'
    Yazdir.allow_tags = True
