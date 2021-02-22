from django.contrib.auth.forms import UserCreationForm
from  django import forms
class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Password Confirmation",widget=forms.PasswordInput(attrs={'class': 'form-control'}))

