from django import forms
from .models import Task, TaskList


class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = '__all__'
        widgets = {
            'created_at': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'created_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }