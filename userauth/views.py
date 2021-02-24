from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import MyUserCreationForm
from student.models import Student
from staff.models import Staff
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
@login_required(login_url='signin')
def dashboard(request):
    if isStaff(request.user.id):
        return render(request,'dashboard.html')
    else:
        return redirect('signout')

def signin(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        u = request.POST['username']
        p = request.POST['pass']
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            print(user.id)
            if(isStaff(user.id)):
                return redirect('dashboard')
            elif(isStudent(user.id)):
                return redirect('studentdashboard')
            return redirect('signout')
        else:
            messages.add_message(request,messages.ERROR,"username or password does not match")
            return redirect('signin')

def signout(request):
    logout(request)
    return redirect('signin')

# helper method

def isStudent(id):
    try:
        s = Student.objects.get(user_id=id)
        return  True
    except:
        return False

def isStaff(id):
    try:
        s = Staff.objects.get(user_id=id)
        return True
    except:
        return False
