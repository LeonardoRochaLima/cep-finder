from rest_framework import serializers
from .models import Cep

class CepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cep
        fields = ('__all__')