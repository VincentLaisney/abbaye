""" apps/accounts/apps.py """

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """ Accounts config """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'
