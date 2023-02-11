from rest_framework import serializers
from .models import Cep, CepsLojaCorr

class CepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cep
        fields = ('__all__')

class CepsLojaCorrSerializer(serializers.ModelSerializer):
    class Meta:
        model = CepsLojaCorr
        fields = ('__all__')