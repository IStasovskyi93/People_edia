from django.db import models
from django.urls import reverse


class Woman(models.Model):
    title = models.CharField(max_length=255, verbose_name='Imię')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Foto')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Ostatnie zmiany')
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    objects = None

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Słynne kobiety'
        verbose_name_plural = 'Słynne kobiety'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Kategoria')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    objects = None

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorii'
        ordering = ['id']
