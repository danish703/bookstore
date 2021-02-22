from django.shortcuts import render

# Create your views here.
def add(request):
    return render(request,'book/add.html')

def booklist(request):
    return render(request,'book/books.html')

def edit(request):
    return render(request,'book/edit.html')

