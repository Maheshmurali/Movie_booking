from django.shortcuts import render,redirect
from .models import UserDetails,AddMovies,Cartdetails


def index(request):
    Movie_list = AddMovies.objects.all()
    p_k = AddMovies.objects.get
    print(p_k)
    return render(request,'index.html',{'Movie_list':Movie_list})

def selection(request,pk):
    get_movie = AddMovies.objects.get(pk=pk)
    Movie_Names = AddMovies.objects.get(pk=pk)
    p_k = pk
    
    if request.POST:
        sNumber = (request.POST.get('snumber'))
        seatNumber = (request.POST.get('seatNumber'))
        cartAmount = (request.POST.get('tamount'))
        print(cartAmount,seatNumber,cartAmount)
        cart = Cartdetails(number=sNumber,seat=seatNumber,amount=cartAmount)
        cart.save()
        return redirect(f'/checkout/{p_k}',Cartdetails)
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

def checkout(request,pk):
    Check_out = AddMovies.objects.get(pk=pk)
    lastUpdate = Cartdetails.objects.latest('updated_at')
    lastUpdate_pk = lastUpdate.pk
    data = Cartdetails.objects.get(pk=lastUpdate_pk)
    return render(request,'checkout.html',{'Check_out':Check_out,'data':data})
    data.delete()
def login(request):
    
    return render(request,'login.html')
