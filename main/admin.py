from __future__ import unicode_literals
from django.contrib import admin
from .models import *


# Register your models here.
# class AtikInline(admin.StackedInline):
#    model = AtikTemel
#    extra = 0
#    max_num = 20


def update_selected(modeladmin, request, queryset):
    for k in queryset:
        k.save()
    return ""


update_selected.short_description = u"Seçilileri Güncelle"


class MainAdminFirma(admin.ModelAdmin):
    # inlines = [AtikInline,]
    list_display = ['FirmaUnvani', 'NACE']
    search_fields = ['NACE', 'FirmaUnvani', 'Il', 'Ilce']

    class Meta:
        model = FirmaBilgileri


admin.site.register(FirmaBilgileri, MainAdminFirma)


class BilesenlerInline(admin.StackedInline):
    model = Bilesenler
    list_display = ['Bilesenadi', 'yüzde']

    class Meta:
        model = Bilesenler


class MainAdminAtik(admin.ModelAdmin):
    list_display = ['AtikKodu', 'Miktar', 'TicariAdi']
    search_fields = ['AtikKodu', 'Miktar']
    list_display_links = ['AtikKodu']
    inlines = [BilesenlerInline]

    actions = (update_selected,)
    actions_on_bottom = True
    actions_on_top = True

    class Meta:
        model = AtikTemel


admin.site.register(AtikTemel, MainAdminAtik)


class HammaddeBilesenlerInline(admin.StackedInline):
    model = HammaddeBilesenler

    class Meta:
        model = HammaddeBilesenler


class MainAdminHammadde(admin.ModelAdmin):
    list_display = ['TicariAdi', 'Miktar']
    inlines = [HammaddeBilesenlerInline]

    class Meta:
        model = Hammadde


admin.site.register(Hammadde, MainAdminHammadde)
