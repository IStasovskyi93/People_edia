from .models import *

menu = [{'title': 'O stronie', 'url_name': 'about'},
        {'title': 'Dodać artykuł', 'url_name': 'add_page'},
        {'title': 'Kontakt', 'url_name': 'contact'},
        {'title': 'Wejść', 'url_name': 'login'}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context


