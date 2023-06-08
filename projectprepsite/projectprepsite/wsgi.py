'''
Version 1.0
Authors: Khadeeja Rizwan and Eddy Wang
Last Updated: February 7, 2023
'''

"""
WSGI config for projectprepsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectprepsite.settings')

application = get_wsgi_application()
