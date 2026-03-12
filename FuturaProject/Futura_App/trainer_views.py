from itertools import groupby
from Futura_App.forms import Evaluationform
from django.shortcuts import render, redirect
from django.contrib import messages
from Futura_App.models import Login,Student,Trainer,Evaluation,Sections,Schedule,Attendance
from django.contrib.auth.decorators import login_required
from datetime import date
from datetime import datetime
import win32print


@login_required(login_url='login_view')
def trainer_page(request):
    return render(request, 'trainertemp/home.html')


def trainer_profile(request):
    user = request.user
    profile = Trainer.objects.filter(user=user)
    return render(request, 'trainertemp/trainer_profile.html', {'profile': profile})


def active1_student(request):
    trainer = Trainer.objects.get(user=request.user)
    details = Student.objects.filter(technology=trainer.technology)
    return render(request, "trainertemp/active.html", {'details': details})


@login_required(login_url='login_view')
def add_evaluation(request, id):
    student = Student.objects.get(id=id)
    sections = Sections.objects.filter(technology=student.technology)
    evaluation_sections = Evaluation.objects.filter(student=student).values_list('evaluation_section__id', flat=True)

    if request.method == 'POST':
        date = request.POST.get('date')
        section_id = request.POST.get('section')
        mcq = int(request.POST.get('mcq', 0))
        mtest = int(request.POST.get('mtest', 0))
        eval = int(request.POST.get('evaluation', 0))
        total = mcq + mtest + eval

        section = Sections.objects.get(pk=section_id)
        obj = Evaluation.objects.create(
            student=student,
            technology=student.technology,
            evaluation_date=date,
            evaluation_section=section,
            mcq=mcq,
            machine_test=mtest,
            evaluation=eval,
            total_mark=total
        )
        obj.save()
        return redirect('view_evaluation')

    # Exclude sections that have already been evaluated by the student
    available_sections = sections.exclude(id__in=evaluation_sections)

    return render(request, 'trainertemp/evaluation_add.html', {'form': student, 'sections': available_sections})


@login_required(login_url='login_view')
def view_evaluation(request):
    trainer = Trainer.objects.filter(user=request.user).first()
    evaluations = Evaluation.objects.filter(technology=trainer.technology).order_by('evaluation_date')
    grouped_evaluations = {}
    for date, group in groupby(evaluations, key=lambda x: x.evaluation_date):
        grouped_evaluations[date] = list(group)
    return render(request, "trainertemp/evaluation_view.html", {'grouped_evaluations': grouped_evaluations})


@login_required(login_url='login_view')
def evaluation_update(request, id):
    eval_update = Evaluation.objects.get(id=id)
    technology = eval_update.technology
    if request.method == 'POST':
        updateform = Evaluationform(request.POST, instance=eval_update)
        if updateform.is_valid():
            total = eval_update.mcq + eval_update.machine_test + eval_update.evaluation
            eval_update.total_mark = total
            eval_update.evaluation_section_id = request.POST.get('section')
            eval_update.save()
            return redirect("view_evaluation")

    else:
        available_sections = Sections.objects.filter(technology=technology)

        # Get the ID of the currently selected section (if any)
        current_section_id = eval_update.evaluation_section_id

        # Retrieve the selected section
        selected_section = None
        other_sections = []
        for section in available_sections:
            if section.id == current_section_id:
                selected_section = section
            else:
                other_sections.append(section)

        # Reorder the sections list to put the selected section first
        ordered_sections = [selected_section] + other_sections

        updateform = Evaluationform(instance=eval_update)

    return render(request, "trainertemp/evaluation_update.html", {'updateform': updateform, 'available_sections': ordered_sections})
#
@login_required(login_url='login_view')
def evaluation_delete(request, id):
    stud_delete = Evaluation.objects.get(id=id)
    if request.method == 'POST':
        stud_delete.delete()
        # messages.info(request, 'Student Details Deleted Successfully')
        return redirect("view_evaluation")


@login_required(login_url='login_view')
def schedule_view(request):
    trainer=Trainer.objects.get(user=request.user)
    details = Schedule.objects.filter(trainers_id=trainer)
    # trial
    # attendance = Attendance.objects.filter(schedule=details)
    # print(attendance)
    return render(request, 'trainertemp/schedule_view.html',{'details':details})


@login_required(login_url='login_view')
def attendance(request,id):
    date_1 = date.today()
    data=Schedule.objects.get(id=id)
    if request.method=='POST':
        stud = request.POST.getlist('checkbox1')
        for i in stud:
            obj=Attendance()
            obj.date=date_1
            obj.schedule=data
            obj.students_id = i
            obj.save()
            return redirect("trainer_schedule_view")
    return render(request,'trainertemp/attendance.html',{'date':date_1,'data':data})




@login_required(login_url='login_view')
def evaluation_report(request):
    trainer = Trainer.objects.filter(user=request.user).first()
    if 'srch' in request.GET:
        s = request.GET['srch']
        evaluations = Evaluation.objects.filter(
            technology=trainer.technology,
            student__name__icontains=s  # Use the related model's field for the search
        ).order_by('evaluation_date')
    else:
        evaluations = Evaluation.objects.filter(
            technology=trainer.technology
        ).order_by('evaluation_date')

    context = {
        "data": evaluations

    }

    return render(request, "trainertemp/evaluation_report.html", context)
