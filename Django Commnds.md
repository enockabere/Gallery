# Create Project Folder

## Activate Virtual Environment
python3 -m venv virtual

## Download Django
python3 -m pip install django

## Create a new Django project and call it Gallery
django-admin startproject gallery .

## We will create an album app then connect it to the gallery project.
django-admin startapp album

## Adding Bootstrap
pip install django-bootstrap-v5 && pip freeze > requirements.txt