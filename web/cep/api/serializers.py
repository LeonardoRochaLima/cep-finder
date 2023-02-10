from rest_framework import serializers
from web.cep import models

class CepSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Cep
        fields = '__all__'