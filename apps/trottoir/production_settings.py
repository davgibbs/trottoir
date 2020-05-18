from .base_settings import *  # noqa

EMAIL_USE_TLS = True
SERVER_EMAIL = 'django@joljardin.com'
EMAIL_HOST = 'localhost'
DEFAULT_FROM_EMAIL = 'support@joljardin.com'

DEBUG = False

PREPEND_WWW = True

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# AWS_STORAGE_BUCKET_NAME = 'myhealthsite'

# IAM account creation for username 'myhealthsite_aws_s3'
# AWS_S3_ACCESS_KEY_ID = get_secret("AWS_S3_ACCESS_KEY_ID")
# AWS_S3_SECRET_ACCESS_KEY = get_secret("AWS_S3_SECRET_ACCESS_KEY")
# IAM account creation for username 'myhealthsite_aws_s3_readonly'
# AWS_S3_ACCESS_KEY_ID_READONLY = get_secret("AWS_S3_ACCESS_KEY_ID_READONLY")
# AWS_S3_SECRET_ACCESS_KEY_READONLY = get_secret("AWS_S3_SECRET_ACCESS_KEY_READONLY")
# AWS_S3_SECURE_URLS = True
# AWS_DEFAULT_ACL = 'private'

# GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-42641358-1'
# GOOGLE_ANALYTICS_DOMAIN = 'webmyhealth.com'

# AWS_S3_CUSTOM_DOMAIN = 's3-eu-west-1.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME
# MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

ALLOWED_HOSTS = ['.joljardin.com', 'www.joljardin.com']

# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            # But the emails are plain text by default - HTML is nicer
            'include_html': True,
        },
        # Log to text files that can be rotated by logrotate
        'default_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/joljardin/default.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        # default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['mail_admins'],
            'propagate': True,
            'level': 'ERROR',
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['default_file'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

# Needed to make source maps when js is compressed
COMPRESS_OFFLINE = True
# COMPRESS_JS_COMPRESSOR = 'wmh_common.uglify.JsUglifySourcemapCompressor'

##############################################################################################################
# RAVEN SETTINGS
##############################################################################################################

# INSTALLED_APPS += ('raven.contrib.django.raven_compat',)

# RAVEN_CONFIG = {
#    'dsn': 'https://75e06e8a0a9643f6a25a9714b89e6e89:2c9a3abafbcd4bc88bc34bf20d898141@sentry.io/107261',
# }

###############################################################################################################

# Set the strict transport security (note added in NGINX)
# SECURE_HSTS_SECONDS = 60 * 60 * 24 * 365  # 1 year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

# Extra Security Settings
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_SSL_REDIRECT = True
# X_FRAME_OPTIONS = 'DENY'

