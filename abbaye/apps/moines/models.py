""" apps/moines/models.py """

from django.db import models


class Monk(models.Model):
    """ Monk model. """
    name = models.CharField(
        max_length=255,
    )
    feast_day = models.IntegerField()
    feast_month = models.IntegerField()
    laundry_number = models.IntegerField(
        blank=True,
        null=True,
    )
    phone_number = models.IntegerField(
        blank=True,
        null=True,
    )
    birthday = models.DateField(
        blank=True,
        null=True,
    )
    entry = models.DateField()
    rank = models.SmallIntegerField(
        default=1,
    )
    habit = models.DateField(
        blank=True,
        null=True,
    )
    profession_temp = models.DateField(
        blank=True,
        null=True,
    )
    profession_perp = models.DateField(
        blank=True,
        null=True,
    )
    priest = models.DateField(
        blank=True,
        null=True,
    )
    death = models.DateField(
        blank=True,
        null=True,
    )
    email = models.EmailField(
        blank=True,
        null=True,
    )
    additional_email = models.EmailField(
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    absences_recipient = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    last_modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name

    def feast_date(self):
        """ Feast date. """
        return '{:02}/{:02}'.format(self.feast_day, self.feast_month)
