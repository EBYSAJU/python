from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect,reverse
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'login/index.html')
def signup(request):
    if request.POST:
        username = request.POST['username']
        fname=request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password= request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"your account has been successfully created")
        return redirect(reverse('signin'))

    return render(request,'login/signup.html')
def signin(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['passsword']
        user=authenticate()
    return render(request,'login/signin.html')
def signout(request):
    pass
