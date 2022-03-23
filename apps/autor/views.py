from rest_framework import viewsets
from apps.autor.models import Autor
from apps.autor.serializer import AutorSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AutorViewSet(viewsets.ModelViewSet):
    """Lista com todos os autores"""
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
