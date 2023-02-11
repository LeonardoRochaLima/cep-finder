import pytest
from ..models import Cep, Estado

@pytest.mark.django_db
def test_cep_model():
    """
        - Este teste verifica a integridade dos registros inseridos na tabela Cep.
        - Valida no momento da inserção e atualização se a flag lojacorr foi atualizada corremente, 
            de acordo com os registros da tabela Estado.
    """
    cep = Cep.objects.create(cep="12345678", logradouro="Rua Teste", localidade="Cidade Teste", uf="ET")
    assert str(cep) == "12345678"
    assert cep.logradouro == "Rua Teste"
    assert cep.localidade == "Cidade Teste"
    assert cep.uf == "ET"
    assert cep.created_at is not None
    assert cep.updated_at is not None
    
    cep.logradouro = "Rua Alterada"
    assert cep.logradouro == "Rua Alterada"
    cep.save()
    assert cep.logradouro == "Rua Alterada"
    assert cep.updated_at > cep.created_at

    estado = Estado.objects.create(uf="ET", nome="ET")
    assert estado.uf == "ET"
    assert estado.nome == "ET"
    assert estado.created_at is not None
    assert estado.updated_at is not None

    cep = Cep.objects.get(cep="12345678")
    assert cep.lojacorr == True

@pytest.mark.django_db
def test_estado_model():
    """
        - Este teste verifica a integridade dos registros inseridos na tabela Estado.
        - Valida no momento da inserção, atualização e remoção se as flags(lojacorr) 
            foram atualizadas corretamente na tabela Cep.
    """
    estado = Estado.objects.create(uf="TS", nome="Estado Teste")
    assert str(estado) == "TS"
    assert estado.nome == "Estado Teste"
    assert estado.created_at is not None
    assert estado.updated_at is not None

    estado.nome = "Estado Alterado"
    assert estado.nome == "Estado Alterado"
    estado.save()
    assert estado.nome == "Estado Alterado"
    assert estado.updated_at > estado.created_at
    
    cep = Cep.objects.create(cep="12345678", logradouro="Rua Teste", localidade="Cidade Teste", uf="TS")
    assert cep.lojacorr is True
    
    estado.delete()
    cep = Cep.objects.get(cep="12345678")
    assert cep.lojacorr is False