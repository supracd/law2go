from base import *

DEBUG = True

# CACHE CONFIG
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploadfiles')
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
