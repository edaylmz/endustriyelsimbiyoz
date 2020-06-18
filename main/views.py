from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, render_to_response
from django.contrib import messages
from django.db.models import Q
from django.views.generic import DetailView

from .forms import *
from django.views.generic.edit import CreateView, UpdateView
from django.db import transaction
from .filters import *


class AtikCreate(CreateView):
    model = AtikTemel
    template_name = 'main/atik_form.html'
    form_class = AtikForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(AtikCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['bilesenler'] = BilesenlerFormSet(self.request.POST, instance=self.object)
        else:
            data['bilesenler'] = BilesenlerFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        bilesenler = context['bilesenler']

        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()

            if bilesenler.is_valid():
                bilesenler.instance = self.object
                bilesenler.save()
        return super(AtikCreate, self).form_valid(form)


class AtikUpdate(UpdateView):
    """redirect metodu yok güncelledikten sonra biyere gitmiyor"""
    model = AtikTemel
    template_name = 'main/atik_form.html'
    form_class = AtikForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(AtikUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['bilesenler'] = BilesenlerFormSet(self.request.POST, instance=self.object)
        else:
            data['bilesenler'] = BilesenlerFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        bilesenler = context['bilesenler']

        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()

            if bilesenler.is_valid():
                bilesenler.instance = self.object
                bilesenler.save()
        return super(AtikUpdate, self).form_valid(form)


def atik_sil(request, id):
    atik = get_object_or_404(AtikTemel, id=id)
    atik.delete()
    return redirect('profil')


def atik_show(request, id):
    atik = get_object_or_404(AtikTemel, id=id)
    bilesenler = Bilesenler.objects.filter(atik=id)
    firma = get_object_or_404(FirmaBilgileri, Firmauye=atik.firma)

    return render(request, 'main/atikgor.html', {"atik": atik, 'bilesenler': bilesenler, 'firma': firma})


def atik_ara(request):
    join = Bilesenler.objects.select_related('atik')
    print(join.query)
    form = AtikFilterForm(request.GET)
    bilesenadi = request.GET.get('bilesenadi')
    il = request.GET.get('il')
    ilce = request.GET.get('ilce')

    yuzde = request.GET.get('yuzde')
    query = join.filter(atik__Il=il).filter(atik__Ilce=ilce). \
        filter(Bilesenadi=bilesenadi).filter(yuzde__range=(yuzde,100)).distinct('atik__TicariAdi')

    context = {'form': form,
               'query': query}
    return render(request, 'main/atikara.html', context)


def hammadde_ara(request):
    join = HammaddeBilesenler.objects.select_related('hammadde')
    print(join.query)
    form = HammaddeFilterForm(request.GET)
    # if request.method == "GET":

    # if form.is_valid():
    il = request.GET.get('il')
    ilce = request.GET.get('ilce')
    bilesenadi = request.GET.get('bilesenadi')
    bilesenadi2 = request.GET.get('bilesenadi2')
    a = join.filter(hammadde__Il=il).filter(hammadde__Ilce=ilce). \
        filter(Bilesenadi=bilesenadi).distinct('hammadde__TicariAdi')

    context = {'form': form,
               'a': a,
               }
    return render(request, 'main/hammaddeara.html', context)


def hammadde_show(request, id):
    hammadde = get_object_or_404(Hammadde, id=id)
    bilesenler = HammaddeBilesenler.objects.filter(hammadde=id)
    firma = get_object_or_404(FirmaBilgileri, Firmauye=hammadde.firma)
    return render(request, 'main/hammaddegor.html', {'hammmadde': hammadde, 'bilesenler': bilesenler, 'firma': firma})


class HammaddeCreate(CreateView):
    model = Hammadde
    template_name = 'main/hammadde_form.html'
    form_class = HammaddeForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(HammaddeCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['hambilesenler'] = HamBilesenFormSet(self.request.POST, instance=self.object)
        else:
            data['hambilesenler'] = HamBilesenFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        hambilesenler = context['hambilesenler']

        with transaction.atomic():
            """userı almıyor"""
            form.instance = self.request.user
            self.object = form.save()

            if hambilesenler.is_valid():
                hambilesenler.instance = self.object
                hambilesenler.save()
        return super(HammaddeCreate, self).form_valid(form)


class HammaddeUpdate(UpdateView):
    """redirect metodu yok güncelledikten sonra biyere gitmiyor"""
    model = Hammadde
    template_name = 'main/hammadde_form.html'
    form_class = HammaddeForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(HammaddeUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['hambilesenler'] = HamBilesenFormSet(self.request.POST, instance=self.object)
        else:
            data['hambilesenler'] = HamBilesenFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        hambilesenler = context['hambilesenler']

        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()

            if hambilesenler.is_valid():
                hambilesenler.instance = self.object
                hambilesenler.save()
        return super(HammaddeUpdate, self).form_valid(form)


def hammadde_sil(request, id):
    hammadde = get_object_or_404(Hammadde, id=id)
    hammadde.delete()
    return redirect('profiltuketici')


def main_UreticiBilgileri(request):
    form = FirmaForm(request.POST or None)
    if form.is_valid():
        firma = form.save(commit=False)
        firma.Firmauye = request.user
        firma.save()

        messages.success(request, "Firma başarıyla eklendi")
        return redirect("anasayfa")
    context = {
        'form': form,
        'title': 'Atık Üreticisi Ekle'
    }
    return render(request, 'main/form.html', context)


def firma_update(request):
    firma = FirmaBilgileri.objects.get(Firmauye=request.user.id)
    form = FirmaForm(request.POST or None, instance=firma)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
        'title': 'Firma Bilgileri Düzenle'
    }
    return render(request, 'main/form.html', context)


def firma_show(request):
    firma = FirmaBilgileri.objects.get(Firmauye=request.user.id)
    context = {
        'firma': firma
    }
    return render(request, 'main/firmaetiket.html', context)


def firma_gor(request, id):
    firma = get_object_or_404(FirmaBilgileri, id=id)
    context = {
        'firma': firma
    }
    return render(request, 'main/firmaetiket.html', context)


def main_profil(request):
    ad = request.user.get_username().upper()
    y = FirmaBilgileri.objects.get(Firmauye=request.user.id)
    x = y.FirmaUnvani
    atiklar = AtikTemel.objects.filter(firma=request.user.id)
    context = {
        'ad': ad,
        'x': x,
        'atiklar': atiklar,

    }
    return render(request, 'main/profil.html', context)


def profil_tuketici(request):
    ad = request.user.get_username().upper()
    y = FirmaBilgileri.objects.get(Firmauye=request.user.id)
    x = y.FirmaUnvani
    hammaddeler = Hammadde.objects.filter(firma=request.user.id)
    context = {
        'ad': ad,
        'x': x,
        'hammaddeler': hammaddeler,
    }

    return render(request, 'main/profiltuketici.html', context)
