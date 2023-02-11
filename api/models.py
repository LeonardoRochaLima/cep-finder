from django.db import models
from django.utils import timezone
import pytz

# Create your models here.

class Cep(models.Model):
    cep = models.CharField(max_length=9, unique=True, primary_key=True)
    logradouro = models.CharField(max_length=100, blank=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True)
    localidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    ibge = models.CharField(max_length=10, blank=True, null=True)
    gia = models.CharField(max_length=10, blank=True, null=True)
    ddd = models.CharField(max_length=3, blank=True, null=True)
    siafi = models.CharField(max_length=10, blank=True, null=True)
    lojacorr = models.BooleanField(default=False)
    created_at = models.CharField(max_length=100)
    updated_at = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.created_at = timezone.now().strftime("%d-%m-%Y %H:%M:%S")
        self.updated_at = timezone.now().strftime("%d-%m-%Y %H:%M:%S")
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.cep} ({self.created_at}) ({self.updated_at})"

class Estado(models.Model):
    uf = models.CharField(max_length=9, unique=True, primary_key=True)
    nome = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)
    updated_at = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.created_at = timezone.now().strftime("%d-%m-%Y %H:%M:%S")
        self.updated_at = timezone.now().strftime("%d-%m-%Y %H:%M:%S")
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.uf} ({self.created_at}) ({self.updated_at})"