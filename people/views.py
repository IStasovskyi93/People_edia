from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Woman

menu = ['O stronie', 'Dodać artykuł', 'Kontakt', 'Wejść']


def index(request):
    posts = Woman.objects.all()
    return render(request, 'people/index.html', {'title': 'Główna strona', 'menu': menu, 'woman': posts})


def about(request):
    return render(request, 'people/about.html', {'title': 'O co chodzi', 'menu': menu})


def categories(request, cat_id):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f'<h1>Artykuły po kategoriach</h1><p>{cat_id}</p>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
    return HttpResponse(f'Rok {year}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Strona nie odnaleziona</h1>')

