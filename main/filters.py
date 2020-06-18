import django_filters

from .models import *


"""class HammaddeFilter(django_filters.FilterSet):
    class Meta:
        model = Hammadde
        fields = ['TicariAdi',
                  'Miktar',
                  'Il',
                  'Ilce',
                  ]"""


"""class HamBilesenFilter(django_filters.FilterSet):
    class Meta:
        model = HammaddeBilesenler.objects.select_related('hammadde')
        fields = ['Bilesenadi',
                  'hammadde.il',
                  'hammadde.ilce',
                 ]
"""
