from django import forms
from django.forms import ModelForm, inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit

from main.custom_layout_object import Formset
from .models import *


class FirmaForm(forms.ModelForm):
    class Meta:
        model = FirmaBilgileri

        fields = [
            'FirmaUnvani',
            'NACE',
            'FaaliyetAlani',
            'Adres',
            'Il',
            'Ilce',
            'FirmaTel',
            'Email',
            'WebSitesi',
            'IlgiliAd',
            'IlgiliTel',
            'IlgiliEmail',
        ]


class HammaddeForm(forms.ModelForm):
    class Meta:
        model = Hammadde
        exclude = []

    def __init__(self, *args, **kwargs):
        super(HammaddeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(Div(
            Field('TicariAdi'),
            Field('Miktar'),
            Field('Il'),
            Field('Ilce'),

            Fieldset('Bileşen Ekle',
                     Formset('hambilesenler')),
            HTML("<br>"),
            ButtonHolder(Submit('submit', 'save')),
        ))


class HamBilesenForm(ModelForm):
    class Meta:
        model = HammaddeBilesenler
        exclude = ()


HamBilesenFormSet = inlineformset_factory(Hammadde, HammaddeBilesenler, form=HamBilesenForm,
                                          fields=['Bilesenadi', 'max', 'min', 'yuzde'], extra=1)


class AtikForm(forms.ModelForm):
    class Meta:
        model = AtikTemel
        exclude = ['firma']

    def __init__(self, *args, **kwargs):
        super(AtikForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(Div(
            Field('AtikKodu'),
            Field('FizikselOzellik'),
            Field('Renk'),
            Field('TehlikeOzellik'),
            Field('ProsesBilgi'),
            Field('AtikAnaliz'),
            Field('Miktar'),
            Field('AtikTanim'),
            Field('TicariAdi'),
            Field('ProsesAmac'),
            Field('ProsesAsama'),
            Field('ProsesOzet'),
            Field('EK3B'),
            Field('EK2'),
            Fieldset('Bileşen Ekle',
                     Formset('bilesenler')),
            HTML("<br>"),
            ButtonHolder(Submit('submit', 'save')),
        ))


class BilesenForm(ModelForm):
    class Meta:
        model = Bilesenler
        exclude = ()


BilesenlerFormSet = inlineformset_factory(AtikTemel, Bilesenler, form=BilesenForm,
                                          fields=['Bilesenadi', 'max', 'min', 'yuzde'], extra=1)


class HammaddeFilterForm(forms.Form):
    bilesenadi = forms.CharField()
    bilesenadi2=forms.CharField()
    il = forms.CharField()
    ilce = forms.CharField()

    def clean_ilce(self):
        ilce = self.cleaned_data['ilce']
        return ilce

    def clean_il(self):
        il = self.cleaned_data['il']
        return il

    def clean_bilesenadi(self):
        bilesenadi = self.cleaned_data['bilesenadi']
        return bilesenadi
    def clean_bilesenadi2(self):
        bilesenadi2 = self.cleaned_data['bilesenadi2']


class AtikFilterForm(forms.Form):
    """CHOICES=(
        ('<','<'),
        ('>','>')
    )"""
    bilesenadi = forms.CharField()
    yuzde = forms.IntegerField()
    il = forms.CharField()
    ilce = forms.CharField()

    def clean_bilesenadi(self):
        bilesenadi = self.cleaned_data['bilesenadi']
        return bilesenadi

    def clean_yuzde(self):
        yuzde=self.cleaned_data['yuzde']
        return yuzde

    def clean_il(self):
        il = self.cleaned_data['il']
        return il

    def clean_ilce(self):
        ilce = self.cleaned_data['ilce']
        return ilce
