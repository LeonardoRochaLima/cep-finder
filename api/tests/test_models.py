import pytest
from ..models import Cep, Estado

@pytest.mark.django_db
def test_cep_model():
    # Cria um objeto Cep
    cep = Cep.objects.create(cep="12345678", logradouro="Rua Teste", localidade="Cidade Teste", uf="ET")
    # Verifica se o registro inserido em Cep está correto
    assert str(cep) == "12345678"
    assert cep.logradouro == "Rua Teste"
    assert cep.localidade == "Cidade Teste"
    assert cep.uf == "ET"
    assert cep.created_at is not None
    assert cep.updated_at is not None
    
    # Altera o atributo logradouro do objeto Cep
    cep.logradouro = "Rua Alterada"
    # Verifica se o atributo logradouro foi realmente alterado antes de salvar
    assert cep.logradouro == "Rua Alterada"
    cep.save()
    # Verifica se o atributo logradouro foi realmente alterado após save() salvar
    assert cep.logradouro == "Rua Alterada"
    # Verifica se o atributo updated_at é maior que o atributo created_at, o que indica que o objeto foi atualizado
    assert cep.updated_at > cep.created_at

    # Cria um objeto Estado
    estado = Estado.objects.create(uf="ET", nome="ET")
    # Verifica se o registro inserido em Estado está correto
    assert estado.uf == "ET"
    assert estado.nome == "ET"
    assert estado.created_at is not None
    assert estado.updated_at is not None

    # Busca o objeto Cep no banco de dados
    cep = Cep.objects.get(cep="12345678")
    # Verifica se o atributo lojacorr está correto no objeto Cep - Estado(UF) == Cep(UF)
    assert cep.lojacorr == True

@pytest.mark.django_db
def test_estado_model():
    # Cria um objeto Estado
    estado = Estado.objects.create(uf="TS", nome="Estado Teste")
    # Verifica se o registro inserido em Estado está correto
    assert str(estado) == "TS"
    assert estado.nome == "Estado Teste"
    assert estado.created_at is not None
    assert estado.updated_at is not None
    
    # Altera o atributo logradouro do objeto Estado
    estado.nome = "Estado Alterado"
    # Verifica se o atributo logradouro foi realmente alterado antes de salvar
    assert estado.nome == "Estado Alterado"
    estado.save()
    # Verifica se o atributo nome foi realmente alterado após save() salvar
    assert estado.nome == "Estado Alterado"
    # Verifica se o atributo updated_at é maior que o atributo created_at, o que indica que o objeto foi atualizado
    assert estado.updated_at > estado.created_at
    
    # Cria um objeto Cep com o mesmo UF do estado
    cep = Cep.objects.create(cep="12345678", logradouro="Rua Teste", localidade="Cidade Teste", uf="TS")
    # Verifica se o atributo lojacorr está correto no objeto Cep - Estado(UF) == Cep(UF)
    assert cep.lojacorr is True
    
    # Deleta o estado
    estado.delete()
    # Pega o objeto Cep cadastrado anteriormente
    cep = Cep.objects.get(cep="12345678")
    # Verifica se o atributo do objeto foi atualizado corretamente - cep.lojacorr == False
    assert cep.lojacorr is False