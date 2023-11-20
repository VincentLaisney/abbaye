""" apps/imprimerie/models.py """

from django.db.models.deletion import CASCADE
from django.db import models
from django_quill.fields import QuillField


class Memo(models.Model):
    """ Memo model. """
    content = QuillField()
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )


class Client(models.Model):
    """ Client model. """
    quality = models.CharField(
        max_length=25,
    )
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )
    address1 = models.CharField(
        max_length=255,
    )
    address2 = models.CharField(
        max_length=255,
    )
    address3 = models.CharField(
        max_length=255,
    )
    zip = models.CharField(
        max_length=255,
    )
    city = models.CharField(
        max_length=255,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return '{} {} {}'.format(self.quality, self.first_name, self.last_name).lstrip()


class Paper(models.Model):
    """ Element Model. """
    name = models.CharField(
        max_length=255,
    )
    dim1 = models.CharField(
        max_length=3,
    )
    dim2 = models.CharField(
        max_length=3,
    )
    weight = models.IntegerField()
    price = models.DecimalField(
        decimal_places=2,
        max_digits=7,
    )

    def __str__(self):
        return '{} {}g {}x{}'.format(self.name, self.weight, self.dim1, self.dim2)


class Project(models.Model):
    """ Project model. """
    name = models.CharField(
        max_length=255,
    )
    client = models.ForeignKey(
        Client,
        on_delete=CASCADE,
    )
    notes = models.TextField(
        null=True,
        blank=True,
    )
    # quantity_client = models.IntegerField()
    # finition = models.CharField(
    #     max_length=255,
    # )
    # width_finished = models.FloatField()
    # length_finished = models.FloatField()
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Element(models.Model):
    """ Element model. """
    project = models.ForeignKey(
        Project,
        on_delete=CASCADE,
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=255,
    )
    quantity = models.IntegerField()
    color = models.CharField(
        max_length=255,
        choices=[
            ('CMYN', 'CMYN'),
            ('B&W', 'B&W'),
        ],
    )
    paper = models.ForeignKey(
        Paper,
        on_delete=CASCADE,
    )
    paper_cut_into = models.IntegerField()
    paper_dim1_machine = models.FloatField()
    paper_dim2_machine = models.FloatField()
    file_width = models.FloatField()
    file_heigth = models.FloatField()
    #imposition = models.IntegerField()
    number_of_sheets_doc = models.IntegerField()
    #recto_verso = models.BooleanField()
    notes = models.TextField()

    def __str__(self):
        return self.name
