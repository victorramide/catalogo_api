from django.db import models
from django.forms import CharField
from django.db import models
#from apps.catalogo.models import Livro


class Autor(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(null=False, blank=False)
    livros = models.ManyToManyField(
        'catalogo.Livro', blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
