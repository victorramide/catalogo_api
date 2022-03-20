from rest_framework import viewsets
from apps.catalogo.models import Livro
from apps.catalogo.serializer import LivroSerializer


class LivrosViewSet(viewsets.ModelViewSet):
    """Lista todos os livros do catalogo"""
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
