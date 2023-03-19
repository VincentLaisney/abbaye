""" apps/moines/models.py """

from django.db import models

from modules.dates import MONTHS, date_to_french_string


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

    def birthday_french(self):
        """ Date of birth french formatted. """
        return date_to_french_string(self.birthday)

    def entry_french(self):
        """ Date of entry french formatted. """
        return date_to_french_string(self.entry)

    def habit_french(self):
        """ Date of habit french formatted. """
        return date_to_french_string(self.habit)

    def profession_temp_french(self):
        """ Date of prof. temp. french formatted. """
        return date_to_french_string(self.profession_temp)

    def profession_perp_french(self):
        """ Date of prof. perp. french formatted. """
        return date_to_french_string(self.profession_perp)

    def priest_french(self):
        """ Date of ordination french formatted. """
        return date_to_french_string(self.priest)

    def death_french(self):
        """ Date of death french formatted. """
        return date_to_french_string(self.death)

    def feast_date(self):
        """ Feast date. """
        return '{:02}/{:02}'.format(self.feast_day, self.feast_month)
