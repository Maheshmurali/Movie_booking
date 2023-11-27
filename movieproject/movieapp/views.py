from django.shortcuts import render
from .models import UserDetails,AddMovies

def index(request):
    Movie_list = AddMovies.objects.all()
    
    return render(request,'index.html',{'Movie_list':Movie_list})

def selection(request,pk):
    get_movie = AddMovies.objects.get(pk=pk)
    Movie_Names = AddMovies.objects.all()
    print(Movie_Names)
    print(get_movie)
    return render(request,'seatselection.html',{'Movie_Names':Movie_Names})

def register(request,):
    if request.POST:
        name = (request.POST.get('fullname'))
        email = (request.POST.get('email'))
        password = (request.POST.get('password'))
        conpassword = (request.POST.get('con_password'))
        user = UserDetails(fullname=name,email=email,password=password,con_password=conpassword)
        user.save()

    return render(request,'register.html')

def checkout(request):
    return render(request,'checkout.html')

def login(request):
    
    return render(request,'login.html')