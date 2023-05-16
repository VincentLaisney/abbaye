""" apps/polyglotte/models.py """

from django.urls import reverse
from django.db import models


class Verse(models.Model):
    """ Verse model. """
    book = models.CharField(max_length=10)
    chapter = models.IntegerField()
    verse = models.IntegerField()
    txt_hebrew = models.TextField(blank=True, null=True)
    txt_greek = models.TextField(blank=True, null=True)
    txt_latin = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        """ Return absolute url of a verse. """
        return reverse(
            'polyglotte:update',
            kwargs={
                'book': self.book,
                'chapter': self.chapter,
                'verse': self.verse
            }
        )
