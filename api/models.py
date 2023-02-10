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

    def __str__(self):
        return self.cep
