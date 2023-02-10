from django.shortcuts import render
from django.views import View
import requests
from web.cep.models import Cep

# Create your views here.

def get_cep_data(request, cep):
    cep_data = Cep.objects.filter(cep=cep).first()
    if cep_data:
        return render(request, 'cep/cep.html', {'cep': cep_data})
    else: 
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
    
class GetCepData(View):
    def get(self, request, **kwargs):
        cep = kwargs.get('cep')
        try:
            cep_obj = Cep.objects.get(cep=cep)
        except Cep.DoesNotExist:
            response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            cep_data = response.json()
            cep_obj = Cep.objects.create(
                cep=cep_data.get('cep'),
                logradouro=cep_data.get('logradouro'),
                complemento=cep_data.get('complemento'),
                bairro=cep_data.get('bairro'),
                localidade=cep_data.get('localidade'),
                uf=cep_data.get('uf'),
                ibge=cep_data.get('ibge'),
                gia=cep_data.get('gia'),
                ddd=cep_data.get('ddd'),
                siafi=cep_data.get('siafi'),
            )
        return render(request, 'cep.html', {'cep': cep_obj})