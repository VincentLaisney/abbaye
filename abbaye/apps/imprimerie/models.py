""" apps/imprimerie/models.py """

from django.db import models


class Memo(models.Model):
    """ Memo model. """
    content = models.TextField(
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )
