from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def djangoFirst(request):
    return HttpResponse('<h1>Django is a Framework</h1>')

def djangoSecond(request):
    return HttpResponse('<h1>Django is a open source Framework</h1>')