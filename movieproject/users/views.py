from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as authlogin,logout,authenticate

def login(request):
    error_message = None
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user =  authenticate(username=email,password=password)
        if user:
            authlogin(request,user)
            return redirect('index')

        else:
            error_message = "Invalid Email Or Password"
    return render(request,'login.html',{'error_message':error_message})


def register(request,):
    user = None
    error_message = None
    if request.POST:
        name = (request.POST.get('fullname'))
        email = (request.POST.get('email'))
        password = (request.POST.get('password'))
        conpassword = (request.POST.get('con_password'))
        try:
            user = User.objects.create_user(username=email,password=password)
            return redirect ('login')
        except Exception as e:
            error_message = str(e)

    return render(request,'register.html',{'user':user,'error_message':error_message})    


def logoutPage(request):
    logout(request)
    return redirect('index')

