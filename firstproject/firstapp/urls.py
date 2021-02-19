from django.contrib import admin
from django.urls import path

from firstapp import views

urlpatterns = [
    # path('about', views.about, name="about"),
    path('<int:num>', views.print_age, name="age"),
    # path('<str:try1>', views.random_f, name="string_sth"),
    path('home', views.home, name="home"),
    path('about', views.about, name="about"),
    path('search', views.search, name="search")
]