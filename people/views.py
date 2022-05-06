from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Główna strona!")


def categories(request):
    return HttpResponse('<h1>Artykuły po kategoriach</h1>')

