from re import S

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', status=201)


def contato(request):
    return HttpResponse('recipes/contato')


def sobre(request):
    return HttpResponse('recipes/sobre')
