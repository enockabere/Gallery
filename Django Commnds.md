# Create Project Folder

## Activate Virtual Environment
python3 -m venv virtual

## Download Django
python3 -m pip install django && pip freeze > requirements.txt

## Create a new Django project and call it Gallery
django-admin startproject gallery .

## We will create an album app then connect it to the gallery project.
django-admin startapp album

## Adding Bootstrap
pip install django-bootstrap-v5 && pip freeze > requirements.txt

## To alter Postgres Password
ALTER USER user_name WITH PASSWORD 'new_password';

## Install database dependency
pip install psycopg2 && pip freeze > requirements.txt

## Initial Migration
python3 manage.py migrate

# Models

## First we have to run checks to validate to see if the models were defined properly.
python3 manage.py check

## Make Migrations
python3 manage.py makemigrations

## View Migration
python3 manage.py sqlmigrate 0001

## Run Migration
python3 manage.py migrate

NB: Error;
    TypeError: __init__() missing 1 required positional argument: 'on_delete'
**add** on_delete=models.CASCADE (if you have a foreign key on your models)