from django import forms
from musician . models import Musician
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = "__all__"

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserChangeData(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ChangePassword(PasswordChangeForm):
    class Meta:
        model = User
        fields = "__all__"
