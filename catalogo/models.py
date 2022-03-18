from django.db import models
from django.forms import CharField


class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=30)
    isbn = models.CharField(max_length=10)
    quantidade_de_paginas = models.DecimalField(
        max_digits=5, decimal_places=0)
    capa = models.URLField()
    editora = models.CharField(max_length=30)
    edicao = models.DecimalField(max_digits=5, decimal_places=0)
    categoria = models.CharField(max_length=30)
    sinopse = models.TextField()
    data_de_publicacao = models.DateField()

    def __str__(self):
        return self.titulo
