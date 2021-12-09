from django.shortcuts import render
from django.http import HttpResponse
from .models import Lh
from .models import St
# Create your views here.


def index(request):
    # s = 'Список залов\r\n\r\n\r\n'
    # for lh in Lh.objects.order_by('-short_Name'):
    #     s += lh.short_Name + '\r\n' + lh.full_Name + '\r\n\r\n'
    #     return HttpResponse(s, content_type='text/plain; charset=utf-8')
    lhs = Lh.objects.all()
    return render(request, "library/index.html", {'lhs': lhs})



