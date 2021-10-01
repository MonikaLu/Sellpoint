# Sellpoint

Sellpoint is a website that allows users to post advertisements of their products. This is a project created for TDT4140 by group 61.

## To run the project:
**python manage.py runserver** in the folder that contains the manage.py file.

## To update requirements:
**pip freeze > requirements.txt**

A **requirements.txt** file is a file that lists all of the modules needed for the Django project to work.

To activate venv i gitpod: **source venv/Scripts/activate**

## Kjøre tester
For å kjøre tester og generere report:
**coverage run --source='app-navn-her' manage.py test && coverage report && coverage html**
Reports blir genrert i htmlcov-mappe

#### Superuser
name: admin
password: aR5!?kuRTui

### Delete expired reklame
**python manage.py delete_expired**

