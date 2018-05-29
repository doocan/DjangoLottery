#!/bin/sh

cd /root/lottery

python manage.py makemigrations

python manage.py makemigrations dlt django_celery_results django_celery_beat

python manage.py migrate  

python manage.py migrate django_celery_results 

python manage.py migrate django_celery_beat

python manage.py runserver 0.0.0.0:8000