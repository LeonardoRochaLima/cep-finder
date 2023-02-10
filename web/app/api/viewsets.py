from rest_framework import viewsets
from web.app.api import serializers
from web.app import models

class CepViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.CepSerializers
    queryset = models.Cep.objects.all()