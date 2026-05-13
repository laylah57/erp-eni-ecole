# erp-eni-ecole

## Description
Un ERP destiné à simplifier la gestion de l'offre de formations de l'ENI Ecole Informatique.

## Environnement
### Backend
Python Django + Django Rest Framework
### Frontend
Angular app

## Installation
### Cloner le projet
`git clone git@github.com:laylah57/erp-eni-ecole.git` <br>
`cd erp-eni-ecole`<br>

### Démarrer le backend
`cd backend`<br>
`python -m venv venv`<br>
MacOS/Linux<br>
`source venv/bin/activate`<br>
Windows<br>
`venv/Scripts/activate`<br>
`pip install django djangorestframework`<br>
`python manage.py migrate`<br>
`python manage.py runserver`<br>

URL du backend: 
http://127.0.0.1:8000/

### Démarrer le frontend
`cd frontend`<br>
`npm install`<br>
`npm start`<br>

URL du frontend:
http://localhost:4200/



