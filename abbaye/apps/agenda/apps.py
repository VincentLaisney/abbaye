""" apps/agenda/apps.py """

from django.apps import AppConfig


class AgendaConfig(AppConfig):
    """ Agenda config """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.agenda'
