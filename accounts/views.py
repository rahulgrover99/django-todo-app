from django.shortcuts import render, redirect
from .forms import CreateUser
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

from trello_app.models import Task

def home(request):
    return render(request, "accounts/home.html")

def register(request):
    if request.method == "POST":
        form = CreateUser(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUser()
    return render(request, "accounts/register.html", {'form': form})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')

        else:
            messages.error(request, "Username or password combination incorrect!")


    return render(request, "accounts/login.html")

def logout(request):
    auth_logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    user = request.user
    task_lists = user.tasklist_set.all()
    tasks = Task.objects.filter(task_list__in=task_lists)
    return render(request, "accounts/dashboard.html", {'task_lists': task_lists, 'tasks': tasks})

