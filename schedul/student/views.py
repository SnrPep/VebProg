from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hi')

def days(request, day):
    if day == 'monday':
        schedule = {
            'Web': '8:30',
            'Math': '10:10'
        }
        #result = [f"<p>{key}: {value}</p>" for key, value in schedule.items()]
        return render(request, "schedule.html", {"data": schedule})
    return HttpResponse('Error')