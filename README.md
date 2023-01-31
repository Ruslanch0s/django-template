# Django template

1) .env/DEBUG=True
2) python manage.py migrate
3) python manage.py runserver


### Install and Prepare

    git clone <repository_url>
    python3.10 -m venv venv
    pip install -r requirements.txt

    > Create .env file
    > Customize .env file

### Run Dev project

1) DEBUG in .env mast be True
2) RUN celery (tasks manager)

       celery -A tasks_manager worker -l INFO

3) Run Django

       python manage.py runserver

### Run Production project

1) DEBUG in .env mast be False


### Django commands

      django-admin startproject <name_root>
      python manage.py startapp <app_name>
      
      python manage.py runserver
      python manage.py runserver 8080
      python manage.py runserver 0.0.0.0:8080
      
      python manage.py makemigrations
      python manage.py migrate
      puthon manage.py createsuperuser
      
      --settings=config.settings.dev
      --settings=config.settings.prod

### Git commands

Сброс локальных изменений

    git reset --hard HEAD

### Pip commands

    pip install -r requirements.txt
    pip freeze -> requirements.txt 
    pip uninstall <package_name>

## Архитектура

**MVC**

Model - View - Controller

- M - services.py
- V - templates
- C - views.py

/templates - в корневой директории

### TASK_MANAGER

1. Работает на Celery
2. Для работы необходим брокер (Redis, и тд)
3. НЕ передавайте объекты базы данных/ORM в задачу (Например что бы передать User использовать поиск по id)
4.

celery -A tasks_manager worker -l INFO

SHEDULER

celery -A tasks_manager.base beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
