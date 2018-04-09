from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import re_path

from libs.urls import NAME_PATTERN, USERNAME_PATTERN
from plugins import views

plugin_urlpatterns = [
    re_path(r'^notebook/{}/{}/?(?P<path>.*)/?$'.format(USERNAME_PATTERN, NAME_PATTERN),
            views.NotebookView.as_view()),
    re_path(r'^tensorboard/{}/{}/?(?P<path>.*)/?$'.format(USERNAME_PATTERN, NAME_PATTERN),
            views.TensorboardView.as_view()),
]

urlpatterns = format_suffix_patterns(plugin_urlpatterns)
