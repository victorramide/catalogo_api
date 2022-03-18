from rest_framework import viewsets
from catalogo.models import Livro
from catalogo.serializer import LivroSerializer


class LivrosViewSet(viewsets.ModelViewSet):
    """Lista todos os livros do catalogo"""
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
