""" apps/moines/models.py """

from django.db import models

from modules.dates import date_to_french_string


class Monk(models.Model):
    """ Monk model. """
    name = models.CharField(
        max_length=255,
    )
    birthday = models.DateField()
    entry = models.DateField()
    rank = models.SmallIntegerField(
        default=1,
    )
    habit = models.DateField(
        null=True,
    )
    profession_temp = models.DateField(
        null=True,
    )
    profession_perp = models.DateField(
        null=True,
    )
    priest = models.DateField(
        null=True,
    )
    death = models.DateField(
        null=True,
    )
    active = models.BooleanField(
        default=True,
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
