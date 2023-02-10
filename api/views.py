from rest_framework import generics
from rest_framework.response import Response
from .models import Cep
from .serializers import CepSerializer
import requests
from rest_framework.views import APIView

class CepList(generics.ListCreateAPIView):
    serializer_class = CepSerializer
    queryset = Cep.objects.all()

class CreateCEPView(APIView):
    def get(self, request, cep):
        # Remove o hífen do CEP, caso exista - Evitando dados duplicados no banco
        cep = cep.replace("-", "")
        # Faz a requisição à API Viacep
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 200:
            data = response.json()

            # Verifica se o CEP já está cadastrado
            cep_obj = Cep.objects.filter(cep=cep).first()
            if cep_obj:
                # Caso já exista, atualiza os dados
                cep_obj.logradouro = data.get("logradouro")
                cep_obj.complemento = data.get("complemento")
                cep_obj.bairro = data.get("bairro")
                cep_obj.localidade = data.get("localidade")
                cep_obj.uf = data.get("uf")
                cep_obj.ibge = data.get("ibge")
                cep_obj.gia = data.get("gia")
                cep_obj.ddd = data.get("ddd")
                cep_obj.siafi = data.get("siafi")
                cep_obj.save()
            else:
                # Caso não exista, cria um novo registro
                Cep.objects.create(
                    cep=cep,
                    logradouro=data.get("logradouro"),
                    complemento=data.get("complemento"),
                    bairro=data.get("bairro"),
                    localidade=data.get("localidade"),
                    uf=data.get("uf"),
                    ibge=data.get("ibge"),
                    gia=data.get("gia"),
                    ddd=data.get("ddd"),
                    siafi=data.get("siafi"),
                )

            # Retorna o objeto do CEP
            cep_obj = Cep.objects.get(cep=cep)
            serializer = CepSerializer(cep_obj)
            return Response(serializer.data)
        else:
            return Response({"error": "CEP não encontrado"}, status=400)

class CepDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CepSerializer
    queryset = Cep.objects.all()
    lookup_field = 'cep'