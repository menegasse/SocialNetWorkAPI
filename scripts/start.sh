source ../env/bin/activate
source ../.env #if .env file don't exist you need to create it in root directory of project and export the SECRET_KEY
python ../manage.py runserver