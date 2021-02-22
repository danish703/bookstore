from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import MyUserCreationForm
# Create your views here.
def signup(request):
    if request.method=="GET":
        form = MyUserCreationForm()
        context = {
            'form':form
        }
        return render(request,'signup.html',context)
    else:
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            return render(request,'signup.html',{'form':form})

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    else:
        return redirect('signin')

def signin(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        u = request.POST['username']
        p = request.POST['pass']
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('signin')

def signout(request):
    logout(request)
    return redirect('signin')