from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import StudentForm, RadioForm
from .models import  Student
# Create your views here.




def second(request):
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
        return render(request, 'index.html')

def first(request):
    if request.method == 'POST':
        name = request.POST['name']
        mark = request.POST['mark']
        place = request.POST['place']
        student = Student(name=name, mark=mark, place=place)
        student.save()
    return render(request, 'student.html')



def third(request):
    form=StudentForm()
    if request.method == 'POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('secondview')
    return render(request,'student.html',{'form':form})



def studview(request):
    data=Student.objects.all()
    return render(request,'stud_view.html',{'data':data})



def studupdate(request,id):
    stud_up = Student.objects.get(id=id)
    if request.method == 'POST':
        up_form = StudentForm(request.POST,instance=stud_up)
        if up_form.is_valid():
            up_form.save()
            return redirect('studviews')
    else:
        up_form = StudentForm(instance=stud_up)
    return render(request, 'stud_update.html', {'up_form': up_form})


# def reg(request):
#     form = Customerform()
#     if request.method == 'POST':
#         form = Customerform(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_customer = True
#             user.save()
#             # messages.success(request, 'success')
#             # print('submit1')
#             return redirect('studviews')
#     return render(request, 'form.html', {'form': form})

def radiofun(request):
    form = RadioForm()
    if request.method == 'POST':
        form = RadioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('regstr')

    return render(request, 'form.html', {'form': form})


