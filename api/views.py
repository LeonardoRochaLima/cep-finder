from rest_framework import generics
from .models import Cep
from .serializers import CepSerializer

class CepList(generics.ListCreateAPIView):
    serializer_class = CepSerializer
    queryset = Cep.objects.all()

class CepDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CepSerializer
    queryset = Cep.objects.all()