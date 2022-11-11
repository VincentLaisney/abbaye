""" apps/ornitho/models.py """

from django.db import models


class Item(models.Model):
    """ Event model. """
    name = models.CharField(
        max_length=255,
    )
    category = models.CharField(
        max_length=255,
    )
    shortcut = models.CharField(
        max_length=255,
    )
    description = models.TextField(
        null=True,
    )
    sound = models.TextField(
        null=True,
    )
    sound_description = models.TextField(
        null=True,
    )
    where = models.TextField(
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    last_modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name
