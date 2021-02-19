from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def random_f(request, try1):
    return HttpResponse("<h1>Hello World</h1>" + try1)


def print_age(request, num):
    return HttpResponse("Your age is " + str(num))


var = {
    "name": "Rahul",
    "age": "21",
    "tv_shows":{
        'Game of Thrones':'9.3',
        'Blacklist': '8',
        'Suits': '8.5',
        'The Witcher': '8.5'
    }
}

# def about(request):
#     return render(request, "firstapp/main.html", context=var)



def home(request):
    return render(request,'firstapp/home.html')

def search(request):
    return render(request,'firstapp/search.html')

def about(request):
    return render(request,'firstapp/about.html')

