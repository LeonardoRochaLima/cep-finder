from django.db import models

# Create your models here.
class Cep(models.Model):
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    
    class Meta:
        app_label = 'web'

class CepsLojaCorr(models.Model):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=2)
    atua = models.BooleanField(default=False)

    class Meta:
        app_label = 'web'