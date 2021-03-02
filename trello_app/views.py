from django.shortcuts import render, redirect
# Create your views here.
from .models import Task, TaskList
from django.contrib.auth.decorators import login_required
from .forms import TaskListForm, TaskForm

def index(request):
    tasks = Task.objects.all()
    task_lists = TaskList.objects.all()
    return render(request, "trello_app/index.html", {'tasks': tasks, 'task_lists': task_lists})


@login_required(login_url='login')
def add_task_list(request):
    if request.method == "POST":
        name = request.POST['name']
        created_at = request.POST['created_at']
        task_list = TaskList(name=name, created_at=created_at)
        task_list.save()
        return redirect('dashboard')
    return render(request, "trello_app/add_task_list.html")

@login_required(login_url='login')
def add_task_list_2(request):
    if request.method == "POST":
        form = TaskListForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('dashboard')
    else: 
        form = TaskListForm()
    return render(request, "trello_app/add_task_list_2.html", {'form': form})

@login_required(login_url='login')
def add_task(request):
    if request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():

            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, "trello_app/add_task.html", {'form': form})