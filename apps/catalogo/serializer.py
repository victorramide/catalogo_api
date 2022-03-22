from rest_framework import serializers
from apps.catalogo.models import Livro


class LivroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'isbn', 'quantidade_de_paginas',
                  'capa', 'editora', 'edicao', 'categoria', 'sinopse', 'data_de_publicacao']
