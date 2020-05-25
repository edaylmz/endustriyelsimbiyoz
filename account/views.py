from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import LoginForm
from django.contrib.auth import authenticate, login


def account_kayitol(request):
    return render(request, 'account/ kayitol.html', {})


def account_giris(request):
    return render(request, 'account/giris.html', {})


def account_anasayfa(request):
    return render(request, 'account/anasayfa.html', {})


def account_cikis(request):
    return HttpResponse('<b>cikis sayfasi</b>')


"""def account_profil(request,id):
    Uye=get_object_or_404(Uye,id=id)
    context={
    'Uye':Uye,
    }
    return render(request, 'account/../templates/main/profil.html', context)"""
