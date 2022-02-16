web: gunicorn mysite.wsgi:application --log-file - --log-level debug
heroku ps:scale web=1
python manage.py collectstatic --noinput
manage.py migrate