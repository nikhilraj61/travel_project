from django.shortcuts import render,redirect
from django.contrib import messages
# from .models import *
from django.contrib.auth.models import User,auth

# Create your views here.

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username ALLready Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Check your Mail")   
                return redirect('register') 
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                print('User Created')
        else:
            print("password not matched")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return  redirect("/")
        else:
            messages.info(request, 'Invalid User')
            return redirect('login')# if the user is invalid then re-direct To loginpage
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")