from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Kullanıcı adı')
    password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=100, label='Parolayı Doğrula', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'confirm',
        ]

    def clean_confirm(self):
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar eşleşmiyor")
        return confirm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Kullanıcı adını ya da parolayı yanlış girdiniz')
        return super(LoginForm, self).clean()
