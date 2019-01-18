# Presentación de GraphQL

Código fuente de la presentación de GraphQL

## Si deseas instalar el proyecto

```
mkvirtualenv graphql --python=/usr/bin/python3

pip install -r requirements.txt
```

## Si lo deseas hacer desde cero

Seguir el paso anterior
```
rm db.sqlite3
python manage.py makemigrations presentacion
python manage.py migrate
```

## Visualizar el proyecto

```
python manage.py runserver

acceder a 

http://localhost:8000/graphql/
```