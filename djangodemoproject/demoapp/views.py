from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import StudentForm
from .models import Product, Student, Student1


# Create your views here.


def index(request):
    student_details = {'students': [
        {
            'name': 'Anika',
            'year': '2016',
            'status': False
        },
        {
            'name': 'Binika',
            'year': '2015',
            'status': False
        }

    ]}
    return render(request, 'index.html', student_details)


def product_view(request):
    product = Product.objects.all()
    return render(request, 'index1.html', {'product': product})


def student_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        mark = request.POST['mark']
        course = request.POST['coure']
        student = Student1(name=name, mark=mark, course=course)
        student.save()
    return render(request, 'student.html')



def stud(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stud_view')
    return render(request, 'student.html',{'form':form})




def demo(request):
    return render(request,'index.html')