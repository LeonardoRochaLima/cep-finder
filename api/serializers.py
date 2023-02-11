from rest_framework import serializers
from .models import Cep, Estado

class CepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cep
        fields = ('__all__')

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('__all__')