from rest_framework import serializers
from apps.autor.models import Autor


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

    