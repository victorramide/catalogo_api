from rest_framework import viewsets
from apps.autor.models import Autor
from apps.autor.serializer import AutorSerializer


class AutorViewSet(viewsets.ModelViewSet):
    """Lista com todos os autores"""
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
