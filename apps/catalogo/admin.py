from re import search
from django.contrib import admin
from apps.catalogo.models import Livro


class Livros(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'categoria')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 10


admin.site.register(Livro, Livros)
