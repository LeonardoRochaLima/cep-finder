from rest_framework import viewsets
from api.serializers import CepSerializer, EstadoSerializer
from api.models import Cep, Estado

class CepViewSets(viewsets.ModelViewSet):
    serializer_class = CepSerializer
    queryset = Cep.objects.all()
    lookup_field = 'cep'

class EstadoViewSets(viewsets.ModelViewSet):
    serializer_class = EstadoSerializer
    queryset = Estado.objects.all().order_by('uf')
    lookup_field = 'uf'