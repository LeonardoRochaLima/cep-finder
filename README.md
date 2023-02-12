# cep-finder
### Objetivo
O objetivo do projeto era criar uma stack utilizando **docker compose** que contemplasse um projeto em **Python/Django**, **Django Rest Framework** e banco de dados **Postgres**.
- Consumindo os dados da [API VIACEP](https://viacep.com.br/) e armazenando as buscas em banco, criando um CRUD para buscar, exibir, listar e editar os dados adquiridos.
- Criar um codetable com todos os estados em que a Lojacorr atua e se a busca por CEP trouxer um estado que está no codetable, criar uma flag no banco para identificar.
- Criar e documentar testes unitários utilizando [PYTEST](https://docs.pytest.org/en/7.2.x/).
- Alimentar o README.md do projeto com informações das stacks.

#### Começando pela estrutura
##### Banco de dados Postgres
Primeiro eu criei uma base de dados bem simples para que o projeto Django pudesse utilizar. Fazia um tempo que não trabalhava com Postgres, então tive que reaprender alguns conceitos. Instalei no meu Debian e criei uma database.

##### Criando projeto Django Rest Framework
No meu repositório do projeto criei uma **venv** do python para controlar as dependências específicas do meu projeto:
```
python3 -m venv venv
```
Ativei a **venv** através do comando:
```
source venv/bin/activate
```
Instalei as dependências do Python/Django e do Django Rest Framwork:
```
pip install django
pip install djangorestframework
```
Depois criei o projeto Django Rest Framework através do comando:
```
django-admin startproject cepFinder
```
Logo em seguida criei uma API para gerenciar minhas **models** e funções que seriam criadas:
```
django-admin startapp api
```

Após isso já era possível rodar o projeto base do Django Resk Framework. Então parti para criação do **docker compose** que executaria minha base de dados e meu projeto Django.
```docker-compose.yml
version: '3'
services:
  db-postgres-leo:
    image: postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: postgres
  django-leo:
    build: .
    command: python manage.py runserver 0.0.0.0:8900
    volumes:
      - .:/code
    ports:
      - "8900:8900"
    depends_on:
      - db-postgres-leo
  run-script:
    build: .
    command: sh run_script.sh
    volumes:
      - .:/code
    depends_on:
      - django-leo
```