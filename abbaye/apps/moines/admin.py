""" apps/moines/admin.py """

from django.contrib import admin
from .models import Monk

admin.site.register(Monk)
