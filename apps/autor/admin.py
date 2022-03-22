from django.contrib import admin
from apps.autor.models import Autor
# Register your models here.


class Autores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10


admin.site.register(Autor, Autores)
