from __future__ import print_function
from django.http import HttpResponse
from django.conf.urls import url
from django.conf import settings
from django.core.wsgi import get_wsgi_application
import os

import sys
def index(request):
    return HttpResponse('Hello World')

urlpatterns = (
        url(r'^$', index),
        )

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', '{{secret_key}}'),
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')
settings.configure(
        DEBUG = DEBUG,
        SECRET_KEY = SECRET_KEY,
        ROOT_URLCONF = __name__,
        MIDDLEWARE_CLASSES = (
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ),
    )


application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    print (sys.argv)
    execute_from_command_line(sys.argv)
