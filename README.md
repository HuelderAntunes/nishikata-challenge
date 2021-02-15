# Desafio 1 - 13/02/2021

## Sobre a solução
Para tornar o problema mais próximo da realidade criei um Model para representar o produto. Para popular  o BD com os dados fornecidos criei o comando customizado populate.

> Caso precise alterar os dados estão no arquivo `products/data.py`.

Para simplificar a pivotagem das vendas por data utilizei o pacote django-pivot e para renderização da tabela o clássico DataTables.

A lógica do ajax está no arquivo products/static/products/js/main.js.

## Como rodar
Execute os comandos a seguir:
```shell
$ cd nishikata

$ python -m venv env

$ ./env/Scripts/activate

$ pip install -r requirements.txt

$ py ./manage.py makemigrations
$ py ./manage.py migrate

$ py ./manage.py test

$ py ./manage.py populate

$ py ./manage.py runserver
```

Após executado os comandos acesse a tabela App pelo navegador: `http://127.0.0.1:8000/`
