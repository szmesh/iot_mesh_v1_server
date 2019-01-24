from django.http import HttpResponse
from django.shortcuts import render


# default/index/home/welcome page
def welcome_info(request):
    return HttpResponse("Welcome to Mesh iot Platform.")


def welcome(request):
    info = 'Welcome to Mesh iot Platform.'
    return render(request, 'welcome.html', {'data': info})
