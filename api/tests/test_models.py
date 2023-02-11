import pytest
from ..models import Cep, Estado

@pytest.mark.django_db
def test_cep_model():
    cep = Cep.objects.create(cep="12345678", logradouro="Rua Teste", localidade="Cidade Teste", uf="TS")
    assert str(cep) == "12345678"
    assert cep.logradouro == "Rua Teste"
    assert cep.localidade == "Cidade Teste"
    assert cep.uf == "TS"
    assert cep.created_at is not None
    assert cep.updated_at is not None
    
    cep.logradouro = "Rua Alterada"
    assert cep.logradouro == "Rua Alterada"
    cep.save()
    assert cep.updated_at > cep.created_at

@pytest.mark.django_db
def test_estado_model():
    estado = Estado.objects.create(uf="TS", nome="Estado Teste")
    assert str(estado) == "TS"
    assert estado.nome == "Estado Teste"
    assert estado.created_at is not None
    assert estado.updated_at is not None
    
    estado.nome = "Estado Alterado"
    assert estado.nome == "Estado Alterado"
    estado.save()
    assert estado.updated_at > estado.created_at
    
    cep = Cep.objects.create(cep="12345678", logradouro="Rua Teste", localidade="Cidade Teste", uf="TS")
    assert cep.lojacorr is True
    
    estado.delete()
    cep = Cep.objects.get(cep="12345678")
    assert cep.lojacorr is False