from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def fun1(request):
    return render(request,'index.html')


def add_form(request):
    return render(request, 'demo.html')
