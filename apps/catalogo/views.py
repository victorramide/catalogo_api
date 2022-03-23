from rest_framework import viewsets
from apps.catalogo.models import Livro
from apps.catalogo.serializer import LivroSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class LivrosViewSet(viewsets.ModelViewSet):
    """Lista todos os livros do catalogo"""
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
