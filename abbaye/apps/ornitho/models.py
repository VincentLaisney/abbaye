""" apps/ornitho/models.py """

import os

from django.conf import settings
from django.db import models


class Item(models.Model):
    """ Event model. """
    name = models.CharField(
        max_length=255,
    )
    category = models.CharField(
        max_length=255,
    )
    shortcut = models.CharField(
        max_length=255,
    )
    description = models.TextField(
        null=True,
    )
    sound = models.TextField(
        null=True,
    )
    sound_description = models.TextField(
        null=True,
    )
    where = models.TextField(
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

    def jpg_exists(self):
        """ Tests if this item has a jpg. """
        sound = os.path.join(
            os.path.join(settings.BASE_DIR, 'statics'),
            'ornitho/images/',
            self.shortcut
        ) + '.jpg'
        return os.path.exists(sound)

    def mp3_exists(self):
        """ Tests if this item has an mp3. """
        sound = os.path.join(
            os.path.join(settings.BASE_DIR, 'statics'),
            'ornitho/sounds/',
            self.shortcut
        ) + '.mp3'
        return os.path.exists(sound)
