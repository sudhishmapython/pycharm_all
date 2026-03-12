from Futura_App.forms import StudentForm,LoginForm,Trainerform
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def student_reg(request):
    login_form = LoginForm()
    student_form = StudentForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        student_form = StudentForm(request.POST)
        if login_form.is_valid() and student_form.is_valid():
            user = login_form.save(commit=False)
            user.is_student = True
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            messages.info(request, 'Student Registered Successfully')
            return redirect('student_reg')
    return render(request, 'student_reg.html', {'login_form': login_form, 'student_form': student_form})



def trainer_reg(request):
    login_form = LoginForm()
    trainer_form = Trainerform()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        trainer_form = Trainerform(request.POST)
        if login_form.is_valid() and trainer_form.is_valid():
            user = login_form.save(commit=False)
            user.is_trainer = True
            user.save()
            trainer = trainer_form.save(commit=False)
            trainer.user = user
            trainer.save()
            messages.info(request, 'Trainer Registered Successfully')
            return redirect('trainer_reg')
    return render(request, 'trainer_reg.html', {'login_form': login_form, 'trainer_form': trainer_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # print(user)
            login(request, user)
            if user.is_staff:
                return redirect('admin_page')
            elif user.is_student:
                return redirect('student_page')

            elif user.is_trainer:
                return redirect('trainer_page')
        else:
            messages.error(request, 'INVALID CREDENTIALS')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')
