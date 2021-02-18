from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def random_f(request, try1):
    return HttpResponse("<h1>Hello World</h1>" + try1)


def print_age(request, num):
    return HttpResponse("Your age is " + str(num))