from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")

def myname(request):
    return HttpResponse("<h1>Зубарев Константин</h1>")

def groupe(request):
    return HttpResponse("Бин-22-2")

def age(request):
    return HttpResponse("19 лет")

def common(request):
    return HttpResponse("<ul> <li>Зубарев Константин</li> <li>Бин-22-2</li> <li>19 лет</li></ul>")