from django.http import HttpResponse
from django.shortcuts import render, redirect

from demoapp.forms import ProductForm
from demoapp.models import Product


# Create your views here.


def fun1(request):
    return render(request,'index.html')


def add_form(request):
    form=ProductForm()
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('functn1')
    return render(request, 'demo.html',{'form':form})


def read_form(request):
    data=Product.objects.all()
    return render(request, 'demo_read.html',{'data':data})

def update_form(request,id):
    data=Product.objects.get(id=id)

    if request.method == 'POST':
        form=ProductForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form = ProductForm(instance=data)
    return render(request,'edit.html',{'form':form})