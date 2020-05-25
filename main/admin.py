from __future__ import unicode_literals
from django.contrib import admin
from .models import AtikTemel, FirmaBilgileri,BilesenAnaliz


# Register your models here.
#class AtikInline(admin.StackedInline):
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
    list_display = ['FirmaUnvani', 'NACE', 'Konum']
    search_fields = ['NACE', 'FirmaUnvani', 'Il', 'Ilce']
    exclude = ['UyeKodu']

    class Meta:
        model = FirmaBilgileri


admin.site.register(FirmaBilgileri, MainAdminFirma)



class MainAdminAtik(admin.ModelAdmin):
    list_display = ['AtikKodu', 'Miktar']
    search_fields = ['AtikKodu', 'Miktar']
    list_display_links = ['AtikKodu']

    actions = (update_selected,)
    actions_on_bottom = True
    actions_on_top = True

    class Meta:
        model = AtikTemel


admin.site.register(AtikTemel, MainAdminAtik)

class MainAdminBilesen(admin.ModelAdmin):
    list_display = ['TicariAdi', 'AtikTanim']
    search_fields = ['TicariAdi','AtikKodu']
    list_display_links = ['TicariAdi']

    class Meta:
        model= BilesenAnaliz
admin.site.register(BilesenAnaliz,MainAdminBilesen)



