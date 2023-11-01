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
        dates = '{:02}/{:02}/{}-{:02}/{:02}/{}'.format(
            self.date_from.day,
            self.date_from.month,
            self.date_from.year,
            self.date_to.day,
            self.date_to.month,
            self.date_to.year
        )
        dates = dates.split('-')[0] \
            if self.date_to == self.date_from \
            else dates
        return '{} ({})'.format(
            self.name,
            dates,
        )


class Category(models.Model):
    """ Category model. """
    name = models.CharField(
        max_length=255,
    )
    color = models.CharField(
        max_length=255,
    )
    priority = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['priority']
        verbose_name_plural = 'categories'
