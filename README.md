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

### Installer la base de données
- Créer une base de données PostgreSQL. Utiliser `erp_eni_ecole` comme nom de la base de données
- Créer un fichier `.env` dans le dossier `backend/`
- Copier-coller le contenu de `.env.example` dans le fichier `.env` (vous le trouverez dans le dossier `backend/`)
- Dans `.env`, remplacer les variables `DB_USER` et `DB_PASSWORD` avec votre identifiant et mot de passe PostgreSQL

### Démarrer le backend
`cd backend`<br>
`python -m venv venv`<br>
<br>
MacOS/Linux<br>
`source venv/bin/activate`<br>
Windows<br>
`venv/Scripts/activate`<br>
<br>
`pip install -r requirements.txt`<br>
`python -m django --version`<br>

### Tester la connexion à la base de données et effectuer les migrations
- Pour tester la connexion à la base de données, exécuter `python manage.py migrate --plan`
- Si tout va bien, exécuter les migrations `python manage.py migrate`
- Dans votre interface PostgreSQL ou en ligne de commande, exécuter le script `sql/01_roles.sql`

### Lancer le serveur backend
- `python manage.py runserver`
- URL du backend: http://127.0.0.1:8000/

### Démarrer le frontend
`cd frontend`<br>
`npm install`<br>
`npm start`<br>

URL du frontend:
http://localhost:4200/


