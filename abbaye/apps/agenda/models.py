""" apps/agenda/models.py """

from django.db import models


class Event(models.Model):
    """ Event model. """
    name = models.CharField(
        max_length=255,
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE
    )
    date_from = models.DateField()
    date_to = models.DateField()
    comment = models.TextField(
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    last_modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    """ Category model. """
    name = models.CharField(
        max_length=255,
    )
    color = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return '{} ({})'.format(self.name, self.color)

    class Meta:
        verbose_name_plural = 'categories'
