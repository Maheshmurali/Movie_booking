from django.shortcuts import render,redirect
from .models import UserDetails,AddMovies,Cartdetails


def index(request):
    Movie_list = AddMovies.objects.all()
    p_k = AddMovies.objects.get
    if request.POST:
        search = (request.POST.get('search'))
        search_balance = search[1:]
        search_first = search[:1]
        search_first = search_first.upper()
        search_value = search_first+search_balance
        Movie_list = AddMovies.objects.filter(movieName=search_value)

    return render(request,'index.html',{'Movie_list':Movie_list})

def selection(request,pk):
    get_movie = AddMovies.objects.get(pk=pk)
    Movie_Names = AddMovies.objects.get(pk=pk)
    p_k = pk
    
    if request.POST:
        sNumber = (request.POST.get('snumber'))
        seatNumber = (request.POST.get('seatNumber'))
        cartAmount = (request.POST.get('tamount'))
        day = (request.POST.get('day'))
        show = (request.POST.get('show'))
        cart = Cartdetails(number=sNumber,seat=seatNumber,amount=cartAmount,day=day,show=show)
        cart.save()
        return redirect(f'/checkout/{p_k}',Cartdetails)
    return render(request,'seatselection.html',{'Movie_Names':Movie_Names})

   

def checkout(request,pk):
    Check_out = AddMovies.objects.get(pk=pk)
    lastUpdate = Cartdetails.objects.latest('updated_at')
    lastUpdate_pk = lastUpdate.pk
    data = Cartdetails.objects.get(pk=lastUpdate_pk)
    return render(request,'checkout.html',{'Check_out':Check_out,'data':data})
    

def malayalam(request):
    Movie_list= AddMovies.objects.filter(language='Malayalam')
    return render(request,'index.html',{'Movie_list':Movie_list})
def tamil(request):
    Movie_list= AddMovies.objects.filter(language='Tamil')
    return render(request,'index.html',{'Movie_list':Movie_list})
def hindi(request):
    Movie_list= AddMovies.objects.filter(language='Hindi')
    return render(request,'index.html',{'Movie_list':Movie_list})
def english(request):
    Movie_list= AddMovies.objects.filter(language='English')
    return render(request,'index.html',{'Movie_list':Movie_list})

def kerala(request):
    Movie_list= AddMovies.objects.filter(language='Malayalam')
    return render(request,'index.html',{'Movie_list':Movie_list})
def tamilnadu(request):
    Movie_list= AddMovies.objects.filter(language='Tamil')
    return render(request,'index.html',{'Movie_list':Movie_list})

        


