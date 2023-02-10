from django.shortcuts import render
import requests
from web.cep.models import Cep

# Create your views here.

def get_cep_data(request, cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    return render(request, 'cep_data.html', {'data': response.json()})

def get_cep_data(request, cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    data = response.json()
    cep_data, created = Cep.objects.get_or_create(cep=data['cep'])
    cep_data.logradouro = data['logradouro']
    cep_data.bairro = data['bairro']
    cep_data.cidade = data['localidade']
    cep_data.uf = data['uf']
    cep_data.save()
    return render(request, 'cep_data.html', {'data': data})