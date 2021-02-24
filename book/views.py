from django.shortcuts import render,redirect
from .forms import BookForm
from django.contrib import messages
from .models import Book
# Create your views here.
def add(request):
    if request.method=='GET':
        form = BookForm()
        context={
            'form':form
        }
        return render(request,'book/add.html',context)
    else:
        form = BookForm(request.POST,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Book created")
            return redirect('booklist')
        else:
            messages.add_message(request,messages.ERROR,"something went wrong")
            return render(request,'book/add.html',{'form':form})

def booklist(request):
    books = Book.objects.all() # SELECT * from book;
    context ={
        'book':books
    }
    return render(request,'book/books.html',context)

def bookdetails(request,id):
    book = Book.objects.get(pk=id)
    return render(request,'book/details.html',{'book':book})

def edit(request,id):
    book = Book.objects.get(pk=id)
    form = BookForm(request.POST or None,request.FILES or None,instance=book)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,"succesfully updated")
        return redirect('booklist')
    context = {
        'form':form
    }
    return render(request,'book/edit.html',context)

def deleteBook(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.add_message(request,messages.SUCCESS,"deleted successfully")
    return redirect('booklist')

