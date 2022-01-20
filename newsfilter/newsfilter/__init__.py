from __future__ import absolute_import

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from newsfilter.celery_config import celery_app

from newsfilter.connection import env

__all__ = [
    "env",
]
