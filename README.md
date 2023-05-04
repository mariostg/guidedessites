# Guide des sites

Ce projet n'est pas prêt pour déploiement!!

## Installation rapide

python3 -m venv .env
source .env/bin/activate
pip install -r requirement-dev.txt
export DJANGO_SETTINGS_MODULE=main.settings
python manage migrate
django-admin manage.py runserver
