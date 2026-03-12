from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_view')
    else:
        form = TaskForm()
    return render(request, 'task_add.html', {'form': form})

def task_view(request):
    taskdetails = Task.objects.all()
    return render(request, "task_view.html", {'taskdetails': taskdetails})

def task_delete(request, dl):
    taskdelete = Task.objects.get(id=dl)
    taskdelete.delete()
    return redirect("task_view")

def task_update(request, up):
    taskupdate = Task.objects.get(id=up)
    if request.method == 'POST':
        updateForm = TaskForm(request.POST, instance=taskupdate)
        if updateForm.is_valid():
            updateForm.save()
            return redirect("task_view")
    else:
        updateForm = TaskForm(instance=taskupdate)
    return render(request, "task_update.html", {'updateform': updateForm})
