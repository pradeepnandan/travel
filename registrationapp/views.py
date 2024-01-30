from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        authuser=auth.authenticate(username=username,password=password)   # auth is table name
        if authuser is not None:
            auth.login(request,authuser)
            return redirect('/')
        else:
            messages.info(request,'Not Authorised User')
            return redirect('login')
    return render(request, 'login.html')
def register(request):
   if request.method=='POST':
       username=request.POST['username']
       firstname = request.POST['first_name']
       lastname = request.POST['last_name']
       password = request.POST['password']
       cpassword = request.POST['re_password']
       email = request.POST['email']
       if password==cpassword:
           if User.objects.filter(username=username).exists():
               messages.info(request,'Already Username taken')
               return redirect('register')
           elif User.objects.filter(email=email).exists():
               messages.info(request,'Already email taken')
           else:
               user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
               user.save()
               messages.info(request,'User is Added')
               return redirect('login')
       else:
           messages.info(request,'Passwords not matching')
           return redirect('register')
       return redirect('/')
   return render(request,'registrationform.html')

def logout(request):
    auth.logout(request)
    return redirect('/')