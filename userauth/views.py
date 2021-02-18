from django.shortcuts import render

# Create your views here.
def signup(reqeust):
    return render(reqeust,'signup.html')

def signin(reqeust):
    return render(reqeust,'login.html')