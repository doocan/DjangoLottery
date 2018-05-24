#!/bin/sh

cd /root/lottery

python manage.py makemigrations

python manage.py makemigrations dlt

python manage.py migrate  

python manage.py runserver 0.0.0.0:8000