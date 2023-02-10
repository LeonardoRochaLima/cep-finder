from django.db import models

# Create your models here.
class Cep(models.Model):
    cep = models.CharField(max_length=9, unique=True)
    logradouro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    ibge = models.CharField(max_length=10, blank=True, null=True)
    gia = models.CharField(max_length=10, blank=True, null=True)
    ddd = models.CharField(max_length=3, blank=True, null=True)
    siafi = models.CharField(max_length=10, blank=True, null=True)

    def get_cep_data(cep):
        cep_object = Cep.objects.get(cep=cep)
        return cep_object
    
    class Meta:
        app_label = 'web'

class CepsLojaCorr(models.Model):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=2)
    atua = models.BooleanField(default=False)

    class Meta:
        app_label = 'web'