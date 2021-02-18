from django.contrib import admin
from django.urls import path

from firstapp import views

urlpatterns = [
    path('<int:num>', views.print_age),
    path('<str:try1>', views.random_f)
]