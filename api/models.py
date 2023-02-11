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
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.cep}"

class Estado(models.Model):
    uf = models.CharField(max_length=9, unique=True, primary_key=True)
    nome = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        ceps = Cep.objects.filter(uf=self.uf)
        if ceps:
            for cep in ceps:
                cep.lojacorr = True
                cep.save()
        
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        ceps = Cep.objects.filter(uf=self.uf)
        for cep in ceps:
            cep.lojacorr = False
            cep.save()
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return f"{self.uf}"