import os

from django.conf import settings


BEEFY_DEFAULT_HEADERS = {
    'Cache-Control': ('no-cache', 'no-store', )
}

BEEFY_HEADERS = getattr(settings, 'BEEFY_HEADERS', BEEFY_DEFAULT_HEADERS)
