from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def python1(request):
    return HttpResponse('<h1>PYTHON is a programming language</h1>')

def python2(request):
    return HttpResponse('<h1>PYTHON is a functional programming language</h1>')