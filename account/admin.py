from __future__ import unicode_literals
from django.contrib import admin
from django.utils import timezone
from .models import Uye


class AccountAdmin(admin.ModelAdmin):
    list_display = ['UyeKodu', 'ad', 'soyad', 'email', 'Yazdir']
    list_per_page = 20
    search_fields = ['UyeKodu', 'ad', 'soyad']
    exclude = ('kayitTarihi',)
    date_hierarchy = 'kayitTarihi'

    class Meta:
        model = Uye


admin.site.register(Uye, AccountAdmin)
