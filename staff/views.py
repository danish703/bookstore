from django.shortcuts import render,redirect
from .forms import AddStaffForm
from django.contrib.auth.models import User
from .models import Staff
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from userauth.views import isStaff
from book.models import BookOrder
# Create your views here.
@login_required(login_url='signin')
def orderlist(request):
    if isStaff(request.user.id):
        context = {
            'orderlist': BookOrder.objects.all()
        }
        return render(request,'orderlist.html',context)
    else:
        return redirect('signout')



def add(request):
    if request.method=='GET':
        context = {
            'form':AddStaffForm()
        }
        return render(request,'staff/add.html',context)
    else:
        username = request.POST['username']
        email  = request.POST['email']

        firstName  = request.POST['firstname']
        lastName  = request.POST['lastname']
        address  = request.POST['address']
        contactno  = request.POST['contactno']
        try:
            user = User(username=username,email=email)
            user.set_password("nepal@123")
            user.save()

            s = Staff(firstname=firstName,lastname=lastName,
                        contactNo=contactno,address=address,user=user)
            s.save()
            messages.add_message(request,messages.SUCCESS,"Saved successfully")
            return redirect('dashboard')
        except:
            messages.add_message(request,messages.ERROR,"sorry some error occured")
            return render(request,'staff/add.html',{'form':AddStaffForm()})
