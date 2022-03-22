from django.db import models
from django.forms import CharField
from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
