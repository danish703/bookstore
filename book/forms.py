from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    name = forms.CharField(label="Book Name",widget=forms.TextInput(attrs={'class':'form-control'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    isbn = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Book
        fields = '__all__'
