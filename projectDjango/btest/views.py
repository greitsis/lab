# from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
#def index(request):
#    return HttpResponse("Привет! Это твое первое приложение!")

from django.http import HttpResponse
from .models import Bb
from django.shortcuts import render

# def index(request):
#     s = 'Список объявлений\r\n\r\n\r\n'
#     for bb in Bb.objects.order_by('-published'):
#         s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
#         return HttpResponse(s, content_type='text/plain; charset=utf-8')
     

def index(request):
    # bbs = Bb.objects.order_by('-published')
    # return render(request, "btest/index.html", {'bbs': bbs})
    bbs = Bb.objects.all()
    return render(request, "btest/index.html", {'bbs': bbs})

    