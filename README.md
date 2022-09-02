# Projeto_LAIS - ELA
**Tencologias:**
- Python
- PostgreSQL
- HTML
- CSS 

**Instalaçao**

1. Utilzando o terminal clonar o projeto usando o comando:

```
git clone https://github.com/AnnyBeatriz10/Projeto_LAIS.git
```

**Ambiente virtual para testar**

2. Preparar ambiente virtual

```
pip install venv venv
```

**Criar banco**

3. Dentro da pasta bin (windows), utilize o seguinte comando:
 
 ```
pg_ctl -D "C:\Program Files (x86)\PostgreSQL\versao instalada\data" start
```
4. Para criar as tabelas, use o comando:

```
python migrate.py makemirations controller
```

5. Envie o arquivo criado da tabela para o banco:

```
python migrate.py migrate 'numeração do arquivo'
```

**iniciar o servidor da aplicação**

```
python manage.py runserver
```



