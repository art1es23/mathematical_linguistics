from django.apps import AppConfig
from django.conf import settings
import os
import pickle


class TeachersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teachers'