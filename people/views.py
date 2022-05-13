from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import Woman, Category

menu = [{'title': 'O stronie', 'url_name': 'about'},
        {'title': 'Dodać artykuł', 'url_name': 'add_page'},
        {'title': 'Kontakt', 'url_name': 'contact'},
        {'title': 'Wejść', 'url_name': 'login'}]


def index(request):
    posts = Woman.objects.all()

    ctx = {
        'menu': menu,
        'woman': posts,
        'title': 'Strona główna',
        'cat_selected': 0,
    }
    return render(request, 'people/index.html', context=ctx)


def about(request):
    return render(request, 'people/about.html', {'title': 'O co chodzi', 'menu': menu})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Strona nie odnaleziona</h1>')


def addpage(request):
    return HttpResponse('Dodawanie strony')


def login(request):
    return HttpResponse('Autoryzacja')


def contact(request):
    return HttpResponse('Kontakt')


def show_post(request, post_id):
    return HttpResponse(f'Prezentacja artykuła z id = {post_id}')


def show_category(request, cat_id):
    posts = Woman.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    ctx = {
        'menu': menu,
        'woman': posts,
        'title': 'Pokaz po kategoriam',
        'cat_selected': cat_id,
    }
    return render(request, 'people/index.html', context=ctx)
