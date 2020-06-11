from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib import messages

from .forms import *
from django.views.generic.edit import CreateView, UpdateView
from django.db import transaction


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


class atik_update(UpdateView):
    model = AtikTemel


def atik_show(request, id):
    atik = get_object_or_404(AtikTemel, id=id)

    return render(request, 'main/atikgor.html', {"atik": atik})


# def atik_update(request,id):
#    atik= get_object_or_404(AtikTemel,id=id)
#    form= AtikForm(request.POST or None,instance=atik)
#    if form.is_valid():
#        form.save()
#    context={'form': form,
#             }
#    return render(request,'main/form.html',context)

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
            form.instance.created_by = self.request.user
            self.object = form.save()

            if hambilesenler.is_valid():
                hambilesenler.instance = self.object
                hambilesenler.save()
        return super(HammaddeCreate, self).form_valid(form)


def main_UreticiBilgileri(request):
    form = FirmaForm(request.POST or None)
    if form.is_valid():
        firma = form.save(commit=False)
        firma.Firmauye = request.user
        firma.save()

        messages.success(request, "Firma başarıyla eklendi")
        return redirect("profil")
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
