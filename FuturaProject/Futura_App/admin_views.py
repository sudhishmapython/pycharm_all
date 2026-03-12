from itertools import groupby

from django.db.models import Q

from .resourses import PersonResource
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Futura_App.forms import StudentForm,Trainerform,Evaluationform,Scheduleform,Slotform,Technologyform,\
    Sectionsform,Activeform
from Futura_App.models import Student,Trainer,Evaluation,Technologies,Slot,Sections,Schedule,Person
from django.contrib.auth.decorators import login_required
from tablib import Dataset



@login_required(login_url='login_view')
def admin_page(request):
    return render(request, 'admintemp/home.html')


def student_view(request):
    data = Student.objects.all()
    return render(request, 'admintemp/student_view.html', {'data': data})

def student_update(request, id):
    stud_update = Student.objects.get(id=id)
    updateform = StudentForm(instance=stud_update)
    if request.method == 'POST':
        updateform = StudentForm(request.POST,  instance=stud_update)
        if updateform.is_valid():
            updateform.save()
            return redirect("student_view")
    return render(request, "admintemp/student_update.html", {'updateform': updateform})


@login_required(login_url='login_view')
def student_delete(request, id):
    stud_delete = Student.objects.get(id=id)
    if request.method == 'POST':
        stud_delete.delete()
        return redirect("student_view")


def trainer_view(request):
    details = Trainer.objects.all
    # trainerFilter = TrainerFilter(request.GET, queryset=details)
    # details = trainerFilter.qs
    # # print(f"Filtered Queryset: {details}")
    # context = {
    #     'user': details,
    #     # 'trainerFilter': trainerFilter,
    #     'no_matches': not details.exists(),
    # }
    return render(request, 'admintemp/trainer_view.html',  {'details':details})


@login_required(login_url='login_view')
def trainer_update(request, id):
    stud_update = Trainer.objects.get(id=id)
    updateform = Trainerform(instance=stud_update)
    if request.method == 'POST':
        updateform = Trainerform(request.POST, request.FILES, instance=stud_update)
        if updateform.is_valid():
            updateform.save()
            return redirect("trainer_view")
    return render(request, "admintemp/trainer_update.html", {'updateform': updateform})


@login_required(login_url='login_view')
def trainer_delete(request, id):
    stud_delete = Trainer.objects.get(id=id)
    if request.method == 'POST':
        stud_delete.delete()
        return redirect("trainer_view")


@login_required(login_url='login_view')
def add_staff(request, id):
    student = Student.objects.get(id=id)
    trainers = Trainer.objects.all()
    if request.method == 'POST':
        # Get the selected Trainer ID from the form
        selected_trainer_id = request.POST.get('staff')
        # Update the staff field of the student with the selected Trainer ID
        student.staff_id = selected_trainer_id
        student.save()
        return redirect('student_view')
    return render(request, 'admintemp/add_staff.html', {'student': student,'trainers':trainers})

@login_required(login_url='login_view')
def admin_evaluation(request):
    evaluations = Evaluation.objects.all().order_by('evaluation_date')
    grouped_evaluations = {}
    for date, group in groupby(evaluations, key=lambda x: x.evaluation_date):
        grouped_evaluations[date] = list(group)
    return render(request, "admintemp/evaluation_view.html", {'grouped_evaluations': grouped_evaluations})


@login_required(login_url='login_view')
def admin_evaluation_update(request, id):
    eval_update = Evaluation.objects.get(id=id)
    stud=eval_update.student
    tech=eval_update.technology
    updateform = Evaluationform(instance=eval_update)
    if request.method == 'POST':
        updateform = Evaluationform(request.POST, instance=eval_update)
        if updateform.is_valid():
            eval_update.student=stud
            eval_update.technology = tech
            updateform.save()
            return redirect("admin_evaluation")
    return render(request, "admintemp/evaluation_update.html", {'updateform': updateform})

#
@login_required(login_url='login_view')
def admin_evaluation_delete(request, id):
    stud_delete = Evaluation.objects.get(id=id)
    if request.method == 'POST':
        stud_delete.delete()
        # messages.info(request, 'Student Details Deleted Successfully')
        return redirect("admin_evaluation")


@login_required(login_url='login_view')
def add_slot(request):
    form = Slotform()
    if request.method == 'POST':
        form = Slotform(request.POST)
        if form.is_valid():
            form.save()
            # messages.info(request, 'Hospital Added Successfully')
            return redirect('add_slot')
    return render(request, 'admintemp/slot_add.html', {'form': form})


@login_required(login_url='login_view')
def slot_view(request):
    details = Slot.objects.all().order_by('date')
    grouped_slots = {}
    for date, group in groupby(details, key=lambda x: x.date):
        grouped_slots[date] = list(group)
    return render(request, 'admintemp/slot_view.html', {'grouped_slots': grouped_slots})



@login_required(login_url='login_view')
def slot_update(request, id):
    n = Slot.objects.get(id=id)
    if request.method == 'POST':
        form = Slotform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            # messages.info(request, 'Hospital Updated Successfully')
            return redirect('slot_view')
    else:
        form = Slotform(instance=n)
    return render(request, 'admintemp/slot_update.html', {'form': form})
#
@login_required(login_url='login_view')
def slot_delete(request, id):
    slot_delete = Slot.objects.get(id=id)
    if request.method == 'POST':
        slot_delete.delete()
        # messages.info(request, 'Student Details Deleted Successfully')
        return redirect("slot_view")


@login_required(login_url='login_view')
def add_technology(request):
    form = Technologyform()
    if request.method == 'POST':
        form = Technologyform(request.POST)
        if form.is_valid():
            form.save()
            # messages.info(request, 'Hospital Added Successfully')
            return redirect('add_technology')
    return render(request, 'admintemp/technology.html', {'form': form})

@login_required(login_url='login_view')
def technology_view(request):
    details = Technologies.objects.all()
    return render(request, 'admintemp/technology_view.html',{'details':details})


@login_required(login_url='login_view')
def technology_update(request, id):
    n = Technologies.objects.get(id=id)
    if request.method == 'POST':
        form = Technologyform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            # messages.info(request, 'Hospital Updated Successfully')
            return redirect('technology_view')
    else:
        form = Technologyform(instance=n)
    return render(request, 'admintemp/technology_update.html', {'form': form})
#
@login_required(login_url='login_view')
def technology_delete(request, id):
    technology_delete = Technologies.objects.get(id=id)
    if request.method == 'POST':
        technology_delete.delete()
        # messages.info(request, 'Student Details Deleted Successfully')
        return redirect("technology_view")



@login_required(login_url='login_view')
def add_sections(request):
    form = Sectionsform()
    if request.method == 'POST':
        form = Sectionsform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Section Added Successfully')
            return redirect('add_sections')
    return render(request, 'admintemp/sections_add.html', {'form': form})


@login_required(login_url='login_view')
def sections_view(request):
    details = Sections.objects.all()
    return render(request, 'admintemp/sections_view.html',{'details':details})


@login_required(login_url='login_view')
def sections_update(request, id):
    n = Sections.objects.get(id=id)
    if request.method == 'POST':
        form = Sectionsform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            # messages.info(request, 'Hospital Updated Successfully')
            return redirect('sections_view')
    else:
        form = Sectionsform(instance=n)
    return render(request, 'admintemp/sections_update.html', {'form': form})
#
@login_required(login_url='login_view')
def sections_delete(request, id):
    sections_delete = Sections.objects.get(id=id)
    if request.method == 'POST':
        sections_delete.delete()
        # messages.info(request, 'Student Details Deleted Successfully')
        return redirect("sections_view")




def get_filtered_students(request):
    technology_id = request.GET.get('technology_id')
    if technology_id:
        students = Student.objects.filter(technology_id=technology_id)
        student_list = [{'id': student.id, 'name': student.name} for student in students]
        return JsonResponse({'students': student_list})
    else:
        return JsonResponse({'error': 'No technology selected'})
def get_filtered_trainers(request):
    technology_id = request.GET.get('technology_id')
    if technology_id:
        trainers = Trainer.objects.filter(technology_id=technology_id)
        trainer_list = [{'id': trainer.id, 'name': trainer.name} for trainer in trainers]
        return JsonResponse({'trainers': trainer_list})
    else:
        return JsonResponse({'error': 'No technology selected'})

@login_required(login_url='login_view')
def add_schedule(request):
    form = Scheduleform()
    if request.method == 'POST':
        form = Scheduleform(request.POST)
        if form.is_valid():
            schedule_instance = form.save(commit=False)
            schedule_instance.save()  # Save the instance first to get a primary key
            form.save_m2m()  # Save the ManyToMany relation
            return redirect('add_schedule')
    return render(request, 'admintemp/schedule_add.html', {'form': form})


@login_required(login_url='login_view')
def schedule_view(request):
    details = Schedule.objects.all()
    return render(request, 'admintemp/schedule_view.html',{'details':details})


@login_required(login_url='login_view')
def schedule_update(request, id):
    schedule_instance = get_object_or_404(Schedule, id=id)

    if request.method == 'POST':
        form = Scheduleform(request.POST, instance=schedule_instance)
        if form.is_valid():
            form.save()
            return redirect('schedule_view')  # Replace 'sections_view' with your desired URL
    else:
        form = Scheduleform(instance=schedule_instance)

    # Render the template with the form
    return render(request, 'admintemp/schedule_update.html', {'form': form})


@login_required(login_url='login_view')
def schedule_delete(request, id):
    schedule_delete = Schedule.objects.get(id=id)
    if request.method == 'POST':
        schedule_delete.students.clear()
        schedule_delete.delete()
        # messages.info(request, 'Student Details Deleted Successfully')
        return redirect("schedule_view")


@login_required(login_url='login_view')
def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']
        if not new_person.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'upload.html')
        imported_data = dataset.load(new_person.read(), format='xlsx')
        for data in imported_data:
            value = Person(
                name=data[0],
                mod=data[1],
                technology=data[2],
                join_date=data[3],
                duration=data[4],
                staff=data[5],
                month=data[6],

            )
            value.save()
    return render(request, 'admintemp/upload.html')



@login_required(login_url='login_view')
def active_student(request):
    details = Person.objects.all()
    # userFilter = StudentFilter(request.GET, queryset=details)
    # details = userFilter.qs
    # # print(f"Filtered Queryset: {details}")
    # context = {
    #     'user': details,
    #     'userFilter': userFilter,
    #     'no_matches': not details.exists(),
    # }
    return render(request, "admintemp/activelist.html", {'details':details})


@login_required(login_url='login_view')
def active_update(request, id):
    stud_update = Person.objects.get(id=id)
    updateform = Activeform(instance=stud_update)
    if request.method == 'POST':
        updateform = Activeform(request.POST, instance=stud_update)
        if updateform.is_valid():
            updateform.save()
            return redirect("active_student")
    return render(request, "admintemp/active_update.html", {'updateform': updateform})

@login_required(login_url='login_view')
def active_delete(request, id):
    stud_delete = Person.objects.get(id=id)
    if request.method == 'POST':
        stud_delete.delete()
        # messages.info(request, 'Student Details Deleted Successfully')
        return redirect("active_student")

@login_required(login_url='login_view')
def evaluation_report_admin(request):
    if 'srch' in request.GET:
        s = request.GET['srch']
        evaluations = Evaluation.objects.filter(
            Q(student__name__icontains=s) | Q(technology__name__icontains=s)
        ).order_by('evaluation_date')
    else:
        evaluations = Evaluation.objects.all().order_by('evaluation_date')

    context = {
        "data": evaluations

    }

    return render(request, "admintemp/evaluation_report_all.html", context)


