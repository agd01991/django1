"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
# os.system("python /home/std/andrey/django-rest-react/app/manage.py makemigrations")
# os.system("python /home/std/andrey/django-rest-react/app/manage.py migrate")
# os.system("python /home/std/andrey/django-rest-react/app/manage.py collectstatic")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()

