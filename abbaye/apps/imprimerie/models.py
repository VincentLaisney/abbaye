""" apps/imprimerie/models.py """

from django.db.models.deletion import CASCADE
from django.db import models
from django_quill.fields import QuillField


class Work(models.Model):
    """ Work model. """
    content = QuillField()
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )


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
    name = models.CharField(
        max_length=255,
    )
    notes = models.TextField(
        null=True,
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return '{}'.format(self.name).lstrip()


class Paper(models.Model):
    """ Element Model. """
    name = models.CharField(
        max_length=255,
    )
    weight = models.IntegerField()
    dim1 = models.CharField(
        max_length=4,
    )
    dim2 = models.CharField(
        max_length=4,
    )
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
    quantity = models.IntegerField(
        null=True,
        blank=True,
    )
    fixed = models.DecimalField(
        null=True,
        blank=True,
        max_digits=7,
        decimal_places=2,
    )
    notes = models.TextField(
        null=True,
        blank=True,
    )
    paper = models.ForeignKey(
        Paper,
        on_delete=CASCADE,
        null=True,
        blank=True,
    )
    paper_cut_into = models.IntegerField(
        null=True,
        blank=True,
    )
    paper_dim1_machine = models.FloatField(
        null=True,
        blank=True,
    )
    paper_dim2_machine = models.FloatField(
        null=True,
        blank=True,
    )
    margins = models.FloatField(
        null=True,
        blank=True,
    )
    file_width = models.FloatField(
        null=True,
        blank=True,
    )
    file_height = models.FloatField(
        null=True,
        blank=True,
    )
    gutters_width = models.FloatField(
        null=True,
        blank=True,
    )
    gutters_height = models.FloatField(
        null=True,
        blank=True,
    )
    number_of_pages_doc = models.IntegerField(
        null=True,
        blank=True,
    )
    fibers = models.BooleanField(
        null=True,
        blank=True,
    )
    imposition = models.IntegerField(
        null=True,
        blank=True,
    )
    recto_verso = models.BooleanField(
        null=True,
        blank=True,
    )
    color = models.CharField(
        max_length=255,
        choices=[
            ('B&W', 'Noir'),
            ('CMYN', 'CMJN'),
        ],
        null=True,
        blank=True,
    )
    massicot = models.IntegerField(
        null=True,
        blank=True,
    )
    pelliculage = models.IntegerField(
        null=True,
        blank=True,
    )
    rainage = models.IntegerField(
        null=True,
        blank=True,
    )
    encollage = models.IntegerField(
        null=True,
        blank=True,
    )
    agrafage = models.IntegerField(
        null=True,
        blank=True,
    )
    total = models.FloatField(
        null=True,
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name
