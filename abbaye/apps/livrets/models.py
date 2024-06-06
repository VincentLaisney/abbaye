""" apps/livrets/models.py """

from django.db import models


class Day(models.Model):
    """ Day model. """
    ref = models.CharField(
        max_length=25,
    )
    title = models.CharField(
        max_length=250,
    )
    rang = models.CharField(
        null=True,
        blank=True,
        max_length=25,
    )
    precedence = models.SmallIntegerField()
    tierce = models.CharField(
        null=True,
        blank=True,
        max_length=250,
    )
    prayers_mg = models.CharField(
        null=True,
        blank=True,
        max_length=25,
    )
    proper_readings = models.BooleanField()
    readings_cycle = models.SmallIntegerField(
        null=True,
        blank=True,
    )
    preface = models.ForeignKey(
        'Preface',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    preface_name_latin = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    preface_name_french = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    sequence = models.CharField(
        null=True,
        blank=True,
        max_length=25,
    )

    def __str__(self):
        return '{} ({})'.format(self.ref, self.title)


class BMV(models.Model):
    """ BMV model. """
    ref = models.CharField(
        max_length=25,
    )
    title = models.CharField(
        max_length=250,
    )
    cm = models.SmallIntegerField()

    def __str__(self):
        return '{} ({} - CM {})'.format(self.ref, self.title, self.cm)


class Preface(models.Model):
    """ Preface model. """
    ref = models.CharField(
        max_length=25,
    )
    name = models.CharField(
        max_length=250,
    )
    page = models.SmallIntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return '{} ({})'.format(self.ref, self.name)


class Score(models.Model):
    """ Score model. """
    type = models.CharField(
        max_length=2,
    )
    ref = models.CharField(
        max_length=25,
    )
    name = models.CharField(
        max_length=250,
    )
    page = models.SmallIntegerField()

    def __str__(self):
        return '{}_{} ({})'.format(self.type, self.ref, self.name)


class Tierce(models.Model):
    """ Tierce model. """
    page = models.SmallIntegerField()
    antiphon = models.CharField(
        max_length=250,
    )

    def __str__(self):
        return '{} : {}'.format(self.page, self.antiphon)
