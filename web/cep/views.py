from django.shortcuts import render
import requests
from web.cep.models import Cep

# Create your views here.

def get_cep_data(request, cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    if response.status_code == 200:
        data = response.json()
        cep_data = Cep(
            cep=data['cep'],
            logradouro=data['logradouro'],
            complemento=data.get('complemento', ''),
            bairro=data['bairro'],
            localidade=data['localidade'],
            uf=data['uf'],
            ibge=data.get('ibge', ''),
            gia=data.get('gia', ''),
            ddd=data.get('ddd', ''),
            siafi=data.get('siafi', ''),
        )
        cep_data.save()
        return cep_data
    else:
        return None