from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello This is E.C.Greeshma   Regnum: 2347115 ")
    #return render(request,'hello/home.html')
    #return render(request,'hello/form.html')
    return render(request,'hello/about.html')
    