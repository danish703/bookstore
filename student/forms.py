from django import forms
from .models import course
from book.models import BookOrder
class AddStudentForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    course = forms.ChoiceField(choices=course,widget=forms.Select(attrs={'class':'form-control'}))
    contactno = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class BookRequestForm(forms.ModelForm):
    returnDate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    class Meta:
        model = BookOrder
        fields = ['returnDate',]