# scripts/delete_all_questions.py

from ..models import Estado

estados = [
    {"uf": "AL", "nome": "Alagoas"},
    {"uf": "BA", "nome": "Bahia"},
    {"uf": "DF", "nome": "Distrito Federal"},
    {"uf": "ES", "nome": "Espírito Santo"},
    {"uf": "GO", "nome": "Goiás"},
    {"uf": "MG", "nome": "Minas Gerais"},
    {"uf": "MS", "nome": "Mato Grosso do Sul"},
    {"uf": "MT", "nome": "Mato Grosso"},
    {"uf": "PA", "nome": "Pará"},
    {"uf": "PE", "nome": "Pernambuco"},
    {"uf": "PR", "nome": "Paraná"},
    {"uf": "RJ", "nome": "Rio de Janeiro"},
    {"uf": "RS", "nome": "Rio Grande do Sul"},
    {"uf": "SC", "nome": "Santa Catarina"},
    {"uf": "SP", "nome": "São Paulo"}
]

def run():
    for estado in estados:
        exist_estado = Estado.objects.filter(uf=estado['uf']).first()
        if not exist_estado:
            Estado.objects.create(uf=estado['uf'], nome=estado['nome'])


