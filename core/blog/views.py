from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def name_blog(request):
    return HttpResponse("<h1>Зубарев Константин</h1>")

def groupe_blog(request):
    return HttpResponse("Бин-22-2")

def age_blog(request):
    return HttpResponse("19 лет")

def common_blog(request):
    return HttpResponse("<ul> <li>Зубарев Константин</li> <li>Бин-22-2</li> <li>19 лет</li></ul>")