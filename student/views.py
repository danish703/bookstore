from django.shortcuts import render,redirect
from .forms import AddStudentForm
from django.contrib.auth.models import User
from .models import Student
from django.contrib import messages
from userauth.views import isStudent
from django.contrib.auth.decorators import login_required
# Create your views here.
def add(request):
    if request.method=='GET':
        context = {
            'form':AddStudentForm()
        }
        return render(request,'student/add.html',context)
    else:
        username = request.POST['username']
        email  = request.POST['email']

        firstName  = request.POST['firstname']
        lastName  = request.POST['lastname']
        course  = request.POST['course']
        address  = request.POST['address']
        contactno  = request.POST['contactno']
        try:
            user = User(username=username,email=email)
            user.set_password("nepal@123")
            user.save()

            s = Student(firstname=firstName,lastname=lastName,
                        contactNo=contactno,course=course,address=address,user=user)
            s.save()
            messages.add_message(request,messages.SUCCESS,"Saved successfully")
            return redirect('dashboard')
        except:
            messages.add_message(request,messages.ERROR,"sorry some error occured")
            return render(request,'student/add.html',{'form':AddStudentForm()})

@login_required(login_url='signin')
def dashboard(request):
    if isStudent(request.user.id):
        return render(request,'studentdashboard.html')
    else:
        return redirect('signout')