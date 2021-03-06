"""
WSGI config for bellycriativa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application
from mezzanine.utils.conf import real_project_name
import sys

sys.path.insert(0, '/home/brunobbbs/webapps/bellycriativa_site/bellycriativa')

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "%s.settings" % real_project_name("bellycriativa"))

application = Cling(get_wsgi_application())
