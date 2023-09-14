from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by ("-update_at")
    context ={
        'all_tasks': tasks,
    }
    return render(request, "home.html", context)

def add_task(request):
    task = request.POST['task']
    Task.objects.create(task = task)
    return redirect("home")
