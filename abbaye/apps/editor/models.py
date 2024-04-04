""" apps/editor/models.py """

from django.core.validators import MinValueValidator
from django.db import models

from .validators import ean13_validator


class Product(models.Model):
    """ Product model. """
    category = models.CharField(
        max_length=25,
        # db_column='Categorie',
    )
    ref_tm = models.CharField(
        max_length=10,
        # db_column='Ref_TM',
    )
    ean = models.CharField(
        max_length=255,
        # db_column='EAN',
        unique=True,
        error_messages={
            'unique': 'Ce code EAN est déjà utilisé par un autre produit.',
        },
        validators=[
            ean13_validator,
        ],
    )
    title = models.CharField(
        max_length=255,
        # db_column='Titre',
    )
    sub_title = models.CharField(
        max_length=255,
        # db_column='Sous_titre',
    )
    author = models.CharField(
        max_length=255,
        # db_column='Auteur',
    )
    interpreter = models.ForeignKey(
        'Interpreter',
        null=True,
        on_delete=models.CASCADE,
        # db_column='Interprete_CD',
    )
    collection = models.ForeignKey(
        'Collection',
        on_delete=models.CASCADE,
        # db_column='Collection',
    )
    number_in_collection = models.IntegerField(
        # db_column='Num_dans_collection',
        validators=[
            MinValueValidator(0)
        ],
    )
    circulation = models.IntegerField(
        # db_column='Chiffre_tirage',
        validators=[
            MinValueValidator(0)
        ],
    )
    publication = models.DateField(
        # db_column='Date_fin_tirage',
    )
    width = models.IntegerField(
        # db_column='Largeur',
        validators=[
            MinValueValidator(0)
        ],
    )
    height = models.IntegerField(
        # db_column='Hauteur',
        validators=[
            MinValueValidator(0)
        ],
    )
    number_of_pages = models.IntegerField(
        # db_column='Nb_pages',
        validators=[
            MinValueValidator(0)
        ],
    )
    weight = models.IntegerField(
        # db_column='Poids',
        validators=[
            MinValueValidator(0)
        ],
    )
    presentation_product = models.TextField(
        # db_column='Pres_objet',
    )
    presentation_author = models.TextField(
        # db_column='Pres_auteur',
    )
    strong_points = models.TextField(
        # db_column='Points_forts',
    )
    target_audience = models.TextField(
        # db_column='Public_vise',
    )
    coefficient = models.FloatField(
        # db_column='Coefficient',
        validators=[
            MinValueValidator(0)
        ],
    )
    price = models.FloatField(
        # db_column='Prix_public',
        validators=[
            MinValueValidator(0)
        ],
    )
    pght = models.FloatField(
        # db_column='PGHT',
        validators=[
            MinValueValidator(0)
        ],
    )
    recto_img = models.CharField(
        max_length=255,
        # db_column='Recto_img',
    )
    verso_img = models.CharField(
        max_length=255,
        # db_column='Verso_img',
    )
    remarques = models.TextField(
        # db_column='Remarques',
    )

    # class Meta:
    #     managed = False
    #     db_table = 'Objets'

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
        # db_column='Collection',
    )
    issn = models.CharField(
        max_length=10,
        # db_column='ISSN',
    )

    # class Meta:
    #     managed = False
    #     db_table = 'Collections'

    def __str__(self):
        return '{} (ISSN {})'.format(self.name, self.issn)


class Interpreter(models.Model):
    """ Interpreter model. """
    name = models.CharField(
        max_length=50,
        # db_column='Interprete',
    )

    # class Meta:
    #     managed = False
    #     db_table = 'Interpretes_CD'

    def __str__(self):
        return self.name


class Charge(models.Model):
    """ Charge model. """
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        # db_column='ID_objet',
    )
    name = models.CharField(
        max_length=50,
        # db_column='Charge'
    )
    amount = models.FloatField(
        # db_column='Montant',
    )

    # class Meta:
    #     managed = False
    #     db_table = 'Charges'
