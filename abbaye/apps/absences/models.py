""" apps/absences/models.py """

from django.db import models

from apps.moines.models import Monk


class Ticket(models.Model):
    """ Ticket class. """
    monks = models.ManyToManyField(
        Monk,
        related_name='monks',
    )
    destination = models.TextField(
        null=True,
    )
    go_date = models.DateField(
        null=True,
    )
    go_moment = models.CharField(
        max_length=25,
        null=True,
    )
    servants = models.BooleanField(
        null=True,
    )
    picnic = models.BooleanField(
        null=True,
    )
    go_by = models.CharField(
        max_length=25,
        null=True,
    )
    go_station = models.CharField(
        max_length=25,
        null=True,
    )
    go_hour = models.TimeField(
        null=True,
    )
    back_date = models.DateField()
    back_moment = models.CharField(
        max_length=25,
        null=True,
    )
    keep_hot = models.BooleanField()
    back_by = models.CharField(
        max_length=25,
        null=True,
    )
    back_station = models.CharField(
        max_length=25,
        null=True,
    )
    back_hour = models.TimeField(
        null=True,
    )
    ordinary_form = models.BooleanField(
        null=True,
    )
    commentary = models.TextField(
        null=True,
    )
    additional_recipients = models.ManyToManyField(
        Monk,
        related_name='additional_recipients',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    last_modified = models.DateTimeField(
        auto_now=True,
    )

