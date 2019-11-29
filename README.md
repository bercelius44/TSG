

Documentacion API

https://app.swaggerhub.com/apis/DavidPalacios/TSG-CRUD-TEST/1.0.0

Instrucciones de despliegue:

Instalar:

    Python 3
    Django: pip install Django
    Django REST: pip install djangorestframework, pip install markdown, pip install django-filter
    Postgresql python driver: pip install psycopg2
    Node
    npm install -g @angular/cli

Instrucciones:

    Levantar API:

Ir a la carpeta django/restServices/restService y modificar el archivo setings.py con los respectivos datos de la base de datos Postgresql (modificar: NAME, USER, PASSWORD, HOST, PORT):

DATABASES = { 
  'default': { 
      'ENGINE': 'django.db.backends.postgresql', 
      'NAME': 'TSG', 
      'USER': 'postgres', 
      'PASSWORD':'brando44.', 
      'HOST':'localhost', 
      'PORT':'5432', 
  } 
}

Ir a la carpeta django/restServices y ejecutar:

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 8444

Desde la consola (CMD) ir a la carpeta angular/crud y ejecutar:

    ng serve

