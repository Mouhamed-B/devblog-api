# devblog_api/urls.py
from django.urls import path

from devblog_api.views import index


urlpatterns = [
    path('', index),
]