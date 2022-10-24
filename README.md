# Black Clover

Magic Academy API

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands
-   Para correr el proyecto:

        $ sudo docker-compose -f local.yml run --rm django python manage.py migrate
        $ sudo docker-compose -f local.yml run --rm django python manage.py createsuperuser
        $ sudo docker-compose -f local.yml up --build

### Intrucciones
-   Para ultilizar la collecion de postman es necesario ir a http://0.0.0.0:8000/admin y logearse
-   Una vez dentro se debe crear un Token para el usuario creado
-   Copiar token y remplazar la variable user_token al igual que el host de ser necesario.

### Tecnologia:
Se utilizó el project template "cookiecutter-django" ya que la considero una herramienta muy poderosa ya que contiene algunas herramientas utiles:

- Celery: Procesos asincronos y rutinarios.
- Pipeline: Nos ayuda a prevenir commits con codigo no funcional.
- Mailhog: Testeo de mails tanto back como front.
- Docker: El contenedor que nos permite hacer deploy de manera eficaz.
- Postgres: Integra postgres al proyecto sin ningun proceso extra.
- Etc.

### Versiones:
-   Python: 3.9
-   Postgress: 13

### Comentarios
-   Se utilizo signals para identificar cambios post-save.
-   Se entiende que ni docker ni cookie-cutter son parte de la prueba. Sin embargo defiendo mi idea de utilizarlo para un proyecto màs completo.
-   La coleccion de Postman se encuentra en este proyecto con el nombre de "Magic Academy", fue exportada como "Collection v2.1"

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
