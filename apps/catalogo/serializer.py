from rest_framework import serializers
from apps.catalogo.models import Livro


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
