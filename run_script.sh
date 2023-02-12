#!/bin/sh
set -e
echo "Executando o script de população do banco de dados: python manage.py runscript -v3 populate_estados;"
python manage.py runscript -v3 populate_estados
echo "Executando os testes com pytest:"
pytest