from rest_framework import generics
from rest_framework.response import Response
from .models import Cep, CepsLojaCorr
from .serializers import CepSerializer, CepsLojaCorrSerializer
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
            
            # Verifica se o cep a ser cadastrado existe na tabela lojacorr
            cep_obj_lojacorr = CepsLojaCorr.objects.filter(cep=cep).first()

            if cep_obj:
                # Se o CEP for de uma das unidades da lojacorr, adicionamos a flag lojacorr=True
                if cep_obj_lojacorr:
                    cep_obj.lojacorr = True
                
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

                # Se o CEP for de uma das unidades da lojacorr, adicionamos a flag lojacorr=True
                if cep_obj_lojacorr: 
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
                        lojacorr=True
                    )
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

class CepsLojaCorrList(generics.ListCreateAPIView):
    serializer_class = CepsLojaCorrSerializer
    queryset = CepsLojaCorr.objects.all()

class CreateCEPsLojaCorrView(APIView):
    def get(self, request, ceplojacor):
        # Remove o hífen do CEP, caso exista - Evitando dados duplicados no banco
        ceplojacorr = ceplojacor.replace("-", "")

        # Faz a requisição à API Viacep
        response = requests.get(f'https://viacep.com.br/ws/{ceplojacorr}/json/')
        if response.status_code == 200:
            data = response.json()

            # Verifica se o cep a ser cadastrado existe na tabela cep
            cep_obj = Cep.objects.filter(cep=ceplojacorr).first()

            if cep_obj:
                cep_obj.lojacorr = True
                cep_obj.save()

            # Verifica se o CEP já está cadastrado
            cep_obj_lojacorr = CepsLojaCorr.objects.filter(cep=ceplojacorr).first()
            if cep_obj_lojacorr:
                # Caso já exista, atualiza os dados
                cep_obj_lojacorr.logradouro = data.get("logradouro")
                cep_obj_lojacorr.complemento = data.get("complemento")
                cep_obj_lojacorr.bairro = data.get("bairro")
                cep_obj_lojacorr.localidade = data.get("localidade")
                cep_obj_lojacorr.uf = data.get("uf")
                cep_obj_lojacorr.ibge = data.get("ibge")
                cep_obj_lojacorr.gia = data.get("gia")
                cep_obj_lojacorr.ddd = data.get("ddd")
                cep_obj_lojacorr.siafi = data.get("siafi")
                cep_obj_lojacorr.save()
            else:
                # Caso não exista, cria um novo registro
                CepsLojaCorr.objects.create(
                    cep=ceplojacorr,
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

            # Retorna o objeto do CEPLojaCorr
            cep_obj_lojacorr = CepsLojaCorr.objects.get(cep=ceplojacorr)
            serializer = CepsLojaCorrSerializer(cep_obj_lojacorr)
            return Response(serializer.data)
        else:
            return Response({"error": "CEP não encontrado"}, status=400)

class CepsLojaCorrDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CepsLojaCorrSerializer
    queryset = CepsLojaCorr.objects.all()
    lookup_field = 'cep'