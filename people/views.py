from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Główna strona!")


def categories(request, cat_id):
    print(request.GET)
    return HttpResponse(f'<h1>Artykuły po kategoriach</h1><p>{cat_id}</p>')


def archive(request, year):
    return HttpResponse(f'Rok {year}')

