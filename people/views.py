from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .models import Woman, Category
from .forms import AddPostForm
from django.views.generic import ListView, DetailView, CreateView
from .utils import *


class WomanHome(DataMixin, ListView):
    model = Woman
    template_name = 'people/index.html'
    context_object_name = 'woman'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Główna strona')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Woman.objects.filter(is_published=True)


# def index(request):
#     posts = Woman.objects.all()
#
#     ctx = {
#         'menu': menu,
#         'woman': posts,
#         'title': 'Strona główna',
#         'cat_selected': 0,
#     }
#     return render(request, 'people/index.html', context=ctx)


def about(request):
    return render(request, 'people/about.html', {'title': 'O co chodzi', 'menu': menu})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Strona nie odnaleziona</h1>')


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'people/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dodawanie artykułu'
        context['menu'] = menu
        return context

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'people/addpage.html', {'menu': menu, 'title': 'Dodawanie artykułu', 'form': form})


def login(request):
    return HttpResponse('Autoryzacja')


def contact(request):
    return HttpResponse('Kontakt')


class ShowPost(DetailView):
    model = Woman
    template_name = 'people/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(Woman, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'people/post.html', context=context)


class WomanCategory(ListView):
    model = Woman
    template_name = 'people/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Woman.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Kategoria - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

# def show_category(request, cat_id):
#     posts = Woman.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     ctx = {
#         'menu': menu,
#         'woman': posts,
#         'title': 'Pokaz po kategoriam',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'people/index.html', context=ctx)
