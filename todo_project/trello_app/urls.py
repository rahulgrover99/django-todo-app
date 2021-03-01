from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('add_task_list', views.add_task_list, name="add_task_list"),
    path('add_task_list_2', views.add_task_list_2, name="addtasklist2"),
    path('add_task', views.add_task)
]

