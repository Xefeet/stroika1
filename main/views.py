from django.http import HttpResponse
from django.shortcuts import render

def index(request):    
    return render(request, 'main/index.html')


def about(request):
    return render (request, 'main/about.html')

def projects(request):
    return render (request, 'main/projects.html')

def contact(request):
    return render (request, 'main/contact.html')

def types(request):
    return render (request, 'main/types.html')

def building(request):
    return render (request, 'main/building.html')

def engineering(request):
    return render (request, 'main/engineering.html')

def projection(request):
    return render (request, 'main/projection.html')

def decoration(request):
    return render (request, 'main/decoration.html')

def design(request):
    return render (request, 'main/design.html')

def ipoteka(request):
    return render (request, 'main/ipoteka.html')