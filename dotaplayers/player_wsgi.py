import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE","dotaplayers.settings")

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
