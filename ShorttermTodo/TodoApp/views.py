from django.shortcuts import render,redirect
from .forms import StudentForm
from . models import Student

# Create your views here.
# def index(request):
#     form=StudentForm()
#     return render(request,'index.html',{'form':form})



def stud_add(request):
    form=StudentForm()
    stud_details = Student.objects.all()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'index.html',{'form':form,'stud_details':stud_details})


def Student_delete(request,id):
    stud_del=Student.objects.get(id=id)
    stud_del.delete()
    return redirect('/')


def Student_update(request,id):
    stud_up=Student.objects.get(id=id)
    if request.method =='POST':
        up_form=StudentForm(request.POST,request.FILES,instance=stud_up)
        if up_form.is_valid():
            up_form.save()
            return redirect('stud_view')
    else:
        up_form=StudentForm(instance=stud_up)
    return render(request, 'index.html',{'up_form':up_form})













