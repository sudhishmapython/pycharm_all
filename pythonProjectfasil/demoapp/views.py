from django.http import HttpResponse
from django.shortcuts import render, redirect

from demoapp.forms import StudentForm, UserRegister, LoginRegister
from demoapp.models import Student


# Create your views here.
def fun1(request):
    return HttpResponse("hello world")

def fun2(request):
    return render(request,'demo.html')


def index(request):
    return render(request,'index.html')

def formdata(request):
    form=StudentForm()
    if request.method == 'POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return  redirect('index1')
    return render(request,'student.html',{'form':form})


def student_read(request):
    data=Student.objects.all()
    return render(request,'stud_view.html',{'data':data})
def sud_update(request,id):
    data=Student.objects.get(id=id)
    up_form=StudentForm(instance=data)
    if request.method == 'POST':
        up_form=StudentForm(request.POST,instance=data)
        if up_form.is_valid():
            up_form.save()
            return redirect('s_read')
    return  render(request,'stud_up.html',{'up_form':up_form})


def user_reg(request):
    formdata=UserRegister()
    logindata=LoginRegister()
    return render(request, 'user_reg.html', {'formdata': formdata,'logindata':logindata})