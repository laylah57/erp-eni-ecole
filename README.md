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
`git clone git@github.com:laylah57/erp-eni-ecole.git`
`cd erp-eni-ecole`

### Démarrer le backend
`cd backend`
`python -m venv venv`
MacOS/Linux
`source venv/bin/activate`
Windows
`venv/Scripts/activate`
`pip install django djangorestframework`
`python manage.py migrate`
`python manage.py runserver`

URL du backend: 
http://127.0.0.1:8000/

### Démarrer le frontend
`cd frontend`
`npm install`
`npm start`

URL du frontend:
http://localhost:4200/



