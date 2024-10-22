""" apps/moines/models.py """

from django.db import models


class Monk(models.Model):
    """ Monk model. """
    name = models.CharField(
        max_length=255,
    )
    civil_first_name = models.CharField(
        max_length=255,
    )
    civil_last_name = models.CharField(
        max_length=255,
    )
    # Dates:
    birthday = models.DateField(
        blank=True,
        null=True,
    )
    entry = models.DateField()
    rank_entry = models.SmallIntegerField(
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
    feast_day = models.IntegerField()
    feast_month = models.IntegerField()
    # Informations:
    laundry_number = models.IntegerField(
        blank=True,
        null=True,
    )
    phone_number = models.IntegerField(
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
    # Admin fields:
    absolute_rank = models.IntegerField(
        default=4,
    )
    is_abbot = models.BooleanField(
        default=False,
    )
    is_prior = models.BooleanField(
        default=False,
    )
    is_abbot_emerite = models.BooleanField(
        default=False,
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
        if self.is_abbot:
            return 'TRP Abbé'
        elif self.is_prior:
            return 'RP Prieur'
        return self.name

    def feast_date(self):
        """ Feast date. """
        return '{:02}/{:02}'.format(self.feast_day, self.feast_month)

    def feast_date_inverted(self):
        """ Feast date inverted (for sorting). """
        return '{:02}/{:02}'.format(self.feast_month, self.feast_day)
