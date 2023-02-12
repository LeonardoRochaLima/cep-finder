# cep-finder
### Objetivo
O objetivo do projeto era criar uma stack utilizando **docker compose** que contemplasse um projeto em **Python/Django**, **Django Rest Framework** e banco de dados **Postgres**.
- Consumindo os dados da [API VIACEP](https://viacep.com.br/) e armazenando as buscas em banco, criando um CRUD para buscar, exibir, listar e editar os dados adquiridos.
- Criar um codetable com todos os estados em que a Lojacorr atua e se a busca por CEP trouxer um estado que está no codetable, criar uma flag no banco para identificar.
- Criar e documentar testes unitários utilizando [PYTEST](https://docs.pytest.org/en/7.2.x/).
- Alimentar o README.md do projeto com informações das stacks.
#### Como executar?
Para rodar os projetos você precisa ter:
1. [Python](https://www.python.org/) instalado na sua máquina.
2. [Docker](https://docs.docker.com/) instalado na sua máquina.
3. Banco de dados [Postgres](https://www.postgresql.org/docs/).
4. Precisa criar uma base de dados no seu banco [Postgres](https://www.postgresql.org/docs/) e inserir as informações no arquivo **docker-compose.yml**:
    ```
    ...
    db-postgres-cepfinder:
        image: postgres
        environment:
        POSTGRES_USER: <usuario_postegrs>
        POSTGRES_PASSWORD: <senha>
        POSTGRES_DB: <database>
    ...
    ```
5. Alterar o parâmetro `ALLOWED_HOSTS` no arquivo `cepFinder/settings.py`. Estava usando um IP interno, talvez você queira rodar no seu `localhost`:
    ```
    ALLOWED_HOSTS = ['localhost']
    ```
6. Rodar o comando para subir os serviços:
    ```
    docker compose up -d --build
    ```
#### Como interagir com a aplicação?


#### Como o projeto foi estruturado?
##### Banco de dados Postgres
<p align="center">
    <img src="images/postgres.png">
</p>
Primeiro eu criei uma base de dados bem simples para que o projeto Django pudesse utilizar. Fazia um tempo que não trabalhava com Postgres, então tive que reaprender alguns conceitos. Instalei no meu Debian e criei uma database.

##### Django Rest Framework
No meu repositório do projeto criei uma **venv** do python para controlar as dependências específicas do meu projeto:
```
python3 -m venv venv
```
Ativei a **venv** através do comando:
```
source venv/bin/activate
```
Instalei as dependências do **Python/Django** e do **Django Rest Framwork**:
```
pip install django
pip install djangorestframework
```
Depois criei o projeto **Django Rest Framework** através do comando:
```
django-admin startproject cepFinder
```
Logo em seguida criei uma API para gerenciar minhas **models** e funções que seriam criadas:
```
django-admin startapp api
```
##### Docker Compose
Após isso já era possível rodar a base do projeto. Então parti para criação do **docker compose**, que criaria os três serviços necessários para nossa aplicação:
- **db-postegres**. Serviço responsável pela execução da base de dados, possibilitando o registro dos outros serviços.
- **django**. Serviço em **Python/Django**, responsável pela execução das funções da aplicação.
- **run-script**. Serviço responsável por chamar uma função via ***bash*** que popula a tabela **Estado**, com todos os estados em que a Lojacorr atua, com base nas [Unidades pelo Brasil](https://redelojacorr.com.br/unidades/).

Os serviços são co-dependentes, por isso adicionei a opção **depends_on** no **docker-compose.yml**, para que os serviços subam na ordem correta.
```docker-compose.yml
version: '3'
services:
  db-postgres-cepfinder:
    image: postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: postgres
  django-cepfinder:
    build: .
    command: python manage.py runserver 0.0.0.0:8900
    volumes:
      - .:/code
    ports:
      - "8900:8900"
    depends_on:
      - db-postgres-cepfinder
  run-script-cepfinder:
    build: .
    command: sh run_script.sh
    volumes:
      - .:/code
    depends_on:
      - django-cepfinder
```

##### Populando a tabela Estado:
Para popular os dados da tabela **Estado** sempre que a stack sobe, eu configurei um script utilizando a biblioteca `django-extensions`. O serviço `run-script-cepfinder` é responsável por rodar um comando via ***bash*** que chama a execução do script, sempre após todos os outros serviços estarem no ar.

1. Instalei a biblioteca `django-extensions` do **Python**:
```
pip install django-extensions
```
2. Configurei um script para popular a tabela **Estado**. Disponível para visualização em: `api/scripts/populate_estados.py`.
3. Criei o arquivo ***bash*** que chama a execução do script. Disponível para visualização em: `./run_script.sh`.

#### Regras aplicadas:
