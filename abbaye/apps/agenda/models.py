""" apps/agenda/models.py """

from django.db import models


class Event(models.Model):
    """ Event model. """
    name = models.CharField(
        max_length=255,
    )
    category = models.CharField(
        max_length=255,
    )
    date_from = models.DateField()
    date_to = models.DateField()
    comment = models.TextField(
        blank=True,
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
