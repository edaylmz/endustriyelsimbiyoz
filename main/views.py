from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import FirmaBilgileri,AtikTemel


def main_AtikBilgileri(request):
    return render(request, 'main/AtikBilgileri.html', {})


def main_AtikEkle(request):
    return render(request, 'main/AtikBilgileri.html', {})


def main_UreticiBilgileri(request):
    return render(request, 'main/AtikBilgileri.html', {})


def main_profil(request):
    return render(request, 'main/profil.html', {})

def main_BilesenAnaliz(request):
    return render(request,'main/BilesenAnaliz.html',{})


def sayfayiyazdir(request,idsi):

     atik= AtikTemel.objects.get(AtikKodu=idsi)

     Firma = FirmaBilgileri.objects.filter(AtikTemel__id=idsi)

     return render(request,'temel.html',{'atik':atik , 'Firma': Firma})
