from polyaxon.config_settings.apps import *
from polyaxon.config_settings.auditor_apps import AUDITOR_APPS

PROJECT_APPS = AUDITOR_APPS + (
    'hpsearch.apps.HPSearchConfig',
)

INSTALLED_APPS += PROJECT_APPS