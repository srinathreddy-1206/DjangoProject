from __future__ import print_function
import os

from django.conf import settings
import sys

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', '@$iuzgq4!fx66&hip6sx_j_#%-qjys0gh*-2(1z(rx@ekqd+$d'),
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


from django.http import HttpResponse, HttpResponseBadRequest
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django import forms


def index(request):
    return HttpResponse('Hello World')


class ImageForm(forms.Form):
    """
    Form to validate reuested placeholder image.
    """
    height = forms.IntegerField(min_value =1, max_value = 2000)
    width = forms.IntegerField(min_value =1, max_value = 2000)

def placeholder(request, width, height):
    form = ImageForm(height=height, width=width)
    if form.is_valid():
        height = form.cleaned_data['height']
        width = form.cleaned_data['width']
        #TO-DO: Generate image of requested Size.
        return HttpResponse('Ok')
    else:
        return HttpResponseBadRequest('Invalid Image Request')

urlpatterns = (
        url(r'^$', index, name = "homepage"),
        url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder, name="placeholder"),
        )

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    print (sys.argv)
    execute_from_command_line(sys.argv)
