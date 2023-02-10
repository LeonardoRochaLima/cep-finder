from rest_framework import viewsets
from web.cep.api import serializers
from web.cep import models

class CepViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.CepSerializers
    queryset = models.Cep.objects.all()

class CepsLojaCorrViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.CepsLojaCorrSerializers
    queryset = models.CepsLojaCorr.objects.all()