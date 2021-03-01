### What are models
    - Contain all the information about the tables in the database
    - It maps a python object to a table or a row in database

### How model maps a class to database?
    - ORM (Object Relational Mapper)
        - Takes a python object and auto converts to the database language
        - Gives you the freedom to use any database
        - Class -> Table
        - Field -> Column
        - Class object -> Row in database



### Whats the difference migrate and makemigrations?

    - makemigrations -> It creates a script in respect of the changes made to models.py (SQL)
    - migrate -> It runs this script


python3 manage.py shell

>>> from trello_app.models import *
>>> task_list_1 = TaskList(name="College")
2 things were observed 
1. id field of the object was empty
2. That in database, the row was not added


.save() method is used to add a row in database
All the above mentioned issues were resolved.


> Explore query sets -> example: Task.objects.all()


Things to remember!
    - Register models in admin.py (Command: admin.site.register(model.ModelName))
    - Add app name to settings.py
    - Models are child classes of models.Model
    - Use of Dunder functions like str
    - Use of Django shell (python3 manage.py shell)


```py
# models.py
from django.db import models
from django.utils import timezone
# Create your models here.

# Requirements
    # - Tasks 
    #     - content
    #     - creation_date
    #     - deadline
    #     - task_list 
        
    #     - Status 
    #     - completed_on

    #  - Task List
        # - name 
        # - created_at



# Task Table

# id | content | creation_date | deadline | task_list_id | status | completed_on | status


# Task_list
# id | name | created_at


class TaskList(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
   

class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(blank=True, null=True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)


    STATUS_CHOICES = (
        ('P', 'PENDING'),
        ('C', 'COMPLETED'),
        ('IP', 'IN_PROGRESS'),
        ('D', 'DROPPED')
    )
    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES[0], max_length=2)

    def __str__(self):
        return f"{self.content}-{self.task_list}"
    
```



name : ______
created_at : _______


submit


content: ________
created_at: ______
deadline: ______
status: ______
task_list: _____ (dropdown) (display names of all tasklists)

What is the diff bw Get Request and a POST request

add_task_list

1. Add a endpoint in urls.py
2. Add a function in views.py which will be able to do 2 things:
    - Render the form
    - Accepts the POST request and saves that to the database
3. Create a template which is form, that takes in information and sends to that views.py function



For creating add_task form:
1. Add a endpoint in urls.py
2. Add a function in views.py:
    - Query for all present task lists, then render a form which has all tasklists passed as a context
    - Accept the post request
    - Make a query to database to get the python object of TaskList that matches with the name from the POST request Tasklist
    - Task(content, ...... task_list)



```py
# forms.py
from django import forms
from .models import Task


class TaskListForm(forms.Form):
    name = forms.CharField(max_length=50)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

```

```py
#views.py
from django.shortcuts import render, redirect
# Create your views here.
from .models import Task, TaskList
from .forms import TaskListForm, TaskForm

def index(request):
    tasks = Task.objects.all()
    task_lists = TaskList.objects.all()
    return render(request, "trello_app/index.html", {'tasks': tasks, 'task_lists': task_lists})



def add_task_list(request):
    if request.method == "POST":
        name = request.POST['name']
        created_at = request.POST['created_at']
        task_list = TaskList(name=name, created_at=created_at)
        task_list.save()
        return redirect('/')
    return render(request, "trello_app/add_task_list.html")


def add_task_list_2(request):
    if request.method == "POST":
        form = TaskListForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            return redirect('/')
    else: 
        form = TaskListForm()
    return render(request, "trello_app/add_task_list_2.html", {'form': form})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():

            form.save()
            return redirect('/')
    else:
        form = TaskForm()

    return render(request, "trello_app/add_task.html", {'form': form})

```
