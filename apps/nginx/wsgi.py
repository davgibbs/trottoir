import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/home/ubuntu/trottoir/apps')
os.environ['DJANGO_SETTINGS_MODULE'] = 'trottoir.production_settings'
application = get_wsgi_application()
