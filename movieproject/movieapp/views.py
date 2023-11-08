from django.shortcuts import render

def index(request):
    my_movie={'movie_list':[{
        'name' : 'Chavaer',
        'img'  : 'https://th.bing.com/th/id/OIF.beNELSuthZ4sTQsuLzplAA?pid=ImgDet&rs=1',
        'summary' : 'a good movie from kunjakka bobban',
        'rating' : '***'},

        {'name' : 'kanthara',
        'img'  : 'https://www.filmibeat.com/ph-big/2021/08/kantara_16282346622.jpg',
        'summary' : 'Hero Protect Their Tradithion',
        'rating' : '***'},
       {'name' : 'Chavaer',
        'img'  : 'https://th.bing.com/th/id/OIF.beNELSuthZ4sTQsuLzplAA?pid=ImgDet&rs=1',
        'summary' : 'a good movie from kunjakka bobban',
        'rating' : '***'},
        {'name' : 'Chavaer',
        'img'  : 'https://th.bing.com/th/id/OIF.beNELSuthZ4sTQsuLzplAA?pid=ImgDet&rs=1',
        'summary' : 'a good movie from kunjakka bobban',
        'rating' : '***'},
       {'name' : 'Chavaer',
        'img'  : 'https://th.bing.com/th/id/OIF.beNELSuthZ4sTQsuLzplAA?pid=ImgDet&rs=1',
        'summary' : 'a good movie from kunjakka bobban',
        'rating' : '***'},
        {'name' : 'Chavaer',
        'img'  : 'https://th.bing.com/th/id/OIF.beNELSuthZ4sTQsuLzplAA?pid=ImgDet&rs=1',
        'summary' : 'a good movie from kunjakka bobban',
        'rating' : '***'},
       ]
    }
    return render(request,'index.html',my_movie)

def selection(request):
    return render(request,'seatselection.html')