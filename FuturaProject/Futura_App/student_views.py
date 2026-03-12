from django.shortcuts import render, redirect
from django.contrib import messages
from Futura_App.forms import StudentForm,Trainerform
from Futura_App.models import Student,Evaluation,Schedule
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required(login_url='login_view')
def student_page(request):
    labels = []
    mcq_data = []
    machine_test_data = []
    evaluation_data = []
    section_status = {}  # Dictionary to store pass/fail status for each section

    student = Student.objects.get(user=request.user)
    queryset = Evaluation.objects.filter(student=student).order_by('total_mark')

    for evaluation in queryset:
        section_label = str(evaluation.evaluation_section)
        labels.append(section_label)  # Use the evaluation section as the label
        mcq_data.append(evaluation.mcq)
        machine_test_data.append(evaluation.machine_test)
        evaluation_data.append(evaluation.evaluation)

        # Determine pass/fail status for each section
        total_mark = evaluation.total_mark
        if total_mark is not None:
            if section_label not in section_status:
                section_status[section_label] = 'Pass' if total_mark >= 50 else 'Fail'
            else:
                if total_mark < 50:
                    section_status[section_label] = 'Fail'

    return render(request, 'usertemp/home.html', {
        'labels': labels,
        'mcq_data': mcq_data,
        'machine_test_data': machine_test_data,
        'evaluation_data': evaluation_data,
        'section_status': section_status
    })



# def student_page(request):
#     from collections import defaultdict
#
#     labels = []
#     mcq_data = defaultdict(list)
#     machine_test_data = defaultdict(list)
#     evaluation_data = defaultdict(list)
#     section_status = {}
#
#     student = Student.objects.get(user=request.user)
#     queryset = Evaluation.objects.filter(student=student).order_by('evaluation_section')
#
#     for evaluation in queryset:
#         section_label = str(evaluation.evaluation_section)
#         if section_label not in labels:
#             labels.append(section_label)
#
#         mcq_data[section_label].append(evaluation.mcq)
#         machine_test_data[section_label].append(evaluation.machine_test)
#         evaluation_data[section_label].append(evaluation.evaluation)
#
#         # Determine pass/fail status for each section
#         total_mark = evaluation.total_mark
#         if total_mark is not None:
#             if section_label not in section_status:
#                 section_status[section_label] = 'Pass' if total_mark >= 50 else 'Fail'
#             else:
#                 if total_mark < 50:
#                     section_status[section_label] = 'Fail'
#
#
#
#
#     return render(request, 'usertemp/home.html', {
#         'labels': labels,
#         'mcq_data': dict(mcq_data),
#         'machine_test_data': dict(machine_test_data),
#         'evaluation_data': dict(evaluation_data),
#         'section_status': section_status
#     })


@login_required(login_url='login_view')
def user_profile(request):
    user = request.user
    profile = Student.objects.filter(user=user)
    return render(request, 'usertemp/user_profile.html', {'profile': profile})


@login_required(login_url='login_view')
def user_evaluation(request):
    stud=Student.objects.filter(user=request.user).first()
    mark= Evaluation.objects.filter(student=stud)
    return render(request, 'usertemp/evaluation_view.html', {'mark': mark})


@login_required(login_url='login_view')
def schedule_view(request):
    student=Student.objects.get(user=request.user)
    details = Schedule.objects.filter(students=student)
    return render(request, 'usertemp/schedule_view.html',{'details':details})


def chart(request):
    labels = []
    mcq_data = []
    machine_test_data = []
    evaluation_data = []
    student = Student.objects.get(user=request.user)
    queryset = Evaluation.objects.filter(student=student).order_by('total_mark')

    for evaluation in queryset:
        labels.append(str(evaluation.evaluation_section))  # Use the evaluation date as the label
        mcq_data.append(evaluation.mcq)
        machine_test_data.append(evaluation.machine_test)
        evaluation_data.append(evaluation.evaluation)

    return render(request, 'chart.html', {
        'labels': labels,
        'mcq_data': mcq_data,
        'machine_test_data': machine_test_data,
        'evaluation_data': evaluation_data
    })