from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib import messages

from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout


def account_kayitol(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        #parolada sıkıntı var şifreleyemiyor
        user.set_password = password
        user.save()
        new_user = authenticate(username=user.username,password=password)
        login(request, new_user)
        return redirect('anasayfa')
    return render(request, 'account/form.html', {'form': form,'title':'Kayıt Ol'})


def account_giris(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('anasayfa')

    return render(request, 'account/form.html', {'form': form,'title':'Giriş Yap'})


def account_anasayfa(request):
    return render(request, 'account/anasayfa.html', {})


def account_cikis(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız.")
    return redirect("giris")


"""def account_profil(request,id):
    Uye=get_object_or_404(Uye,id=id)
    context={
    'Uye':Uye,
    }
    return render(request, 'account/../templates/main/profil.html', context)"""
