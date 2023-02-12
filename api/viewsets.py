from rest_framework import viewsets
from api.serializers import CepSerializer, EstadoSerializer
from api.models import Cep, Estado
from django.shortcuts import get_object_or_404

class CepViewSets(viewsets.ModelViewSet):
    serializer_class = CepSerializer
    queryset = Cep.objects.all()
    lookup_field = 'cep'

    def get_object(self):
        queryset = self.get_queryset()
        cep = self.kwargs[self.lookup_field].replace('-', '')
        return get_object_or_404(queryset, cep=cep)

class EstadoViewSets(viewsets.ModelViewSet):
    serializer_class = EstadoSerializer
    queryset = Estado.objects.all().order_by('uf')
    lookup_field = 'uf'