""" apps/editor/models.py """

from django.core.validators import MinValueValidator
from django.db import models

from .validators import ean13_validator


class Product(models.Model):
    """ Product model. """
    category = models.CharField(
        max_length=25,
    )
    ref_tm = models.CharField(
        null=True,
        max_length=25,
    )
    ean = models.CharField(
        null=True,
        max_length=255,
        error_messages={
            'unique': 'Ce code EAN est déjà utilisé par un autre produit.',
        },
        validators=[
            ean13_validator,
        ],
    )
    title = models.CharField(
        null=True,
        max_length=255,
    )
    sub_title = models.CharField(
        null=True,
        max_length=255,
    )
    author = models.CharField(
        null=True,
        max_length=255,
    )
    interpreter = models.ForeignKey(
        'Interpreter',
        null=True,
        on_delete=models.CASCADE,
    )
    collection = models.ForeignKey(
        'Collection',
        null=True,
        on_delete=models.CASCADE,
    )
    number_in_collection = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(0)
        ],
    )
    circulation = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(0)
        ],
    )
    publication = models.DateField(
        null=True,
    )
    width = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(0)
        ],
    )
    height = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(0)
        ],
    )
    number_of_pages = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(0)
        ],
    )
    weight = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(0)
        ],
    )
    presentation_product = models.TextField(
        null=True,
    )
    presentation_author = models.TextField(
        null=True,
    )
    strong_points = models.TextField(
        null=True,
    )
    target_audience = models.TextField(
        null=True,
    )
    coefficient = models.FloatField(
        null=True,
        validators=[
            MinValueValidator(0)
        ],
    )
    price = models.FloatField(
        null=True,
        validators=[
            MinValueValidator(0)
        ],
    )
    pght = models.FloatField(
        null=True,
        validators=[
            MinValueValidator(0)
        ],
    )
    recto_img = models.CharField(
        null=True,
        max_length=255,
    )
    verso_img = models.CharField(
        null=True,
        max_length=255,
    )
    remarques = models.TextField(
        null=True,
    )

    def __str__(self):
        designation = ''
        if self.category == 'book':
            if self.ref_tm:
                designation += self.ref_tm
            if self.title:
                if self.ref_tm:
                    designation += ' - '
                designation += self.title
            if self.sub_title:
                if self.title:
                    designation += ' '
                designation += '({})'.format(self.sub_title)

        elif self.category == 'disk':
            if self.ref_tm:
                designation += self.ref_tm
            if self.title:
                if self.ref_tm:
                    designation += ' - '
                designation += self.title
            if self.interpreter:
                designation += ', par {}'.format(self.interpreter.name)

        elif self.category == 'image':
            if self.ref_tm:
                designation += self.ref_tm

        return designation


class Collection(models.Model):
    """ Collection model. """
    name = models.CharField(
        max_length=255,
    )
    issn = models.CharField(
        max_length=10,
    )

    def __str__(self):
        return '{} (ISSN {})'.format(self.name, self.issn)


class Interpreter(models.Model):
    """ Interpreter model. """
    name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.name


class Charge(models.Model):
    """ Charge model. """
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=50,
    )
    amount = models.FloatField(
    )
