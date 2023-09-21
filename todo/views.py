from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task
def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by ("-update_at")
    completed_tasks= Task.objects.filter(is_completed=True)

    context ={
        'all_tasks': tasks,
        'completed_tasks':completed_tasks,
    }
    return render(request, "home.html", context)

def add_task(request):
    task = request.POST['task']
    Task.objects.create(task = task)
    return redirect("home")

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect(home)

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect(home)

def edit(request,pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
        return render(request, 'edit_task.html', context)

def delete(request, id):
    del_task = get_object_or_404(Task, pk=id)
    del_task.delete()
    return redirect('home')


