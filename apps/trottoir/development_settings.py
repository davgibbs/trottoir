from .base_settings import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Compression of the CSS and JS files
COMPRESS_ENABLED = False

# Python dotted path to the WSGI application used by Django's runserver.
# Local Development only.
WSGI_APPLICATION = 'trottoir.wsgi.application'

# Do not send email verification on signup on Local
ACCOUNT_EMAIL_VERIFICATION = 'none'
