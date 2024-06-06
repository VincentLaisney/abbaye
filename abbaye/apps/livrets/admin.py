""" apps/livrets/admin.py """

from django.contrib import admin
from .models import Day, BMV, Preface, Score

admin.site.register(Day)
admin.site.register(BMV)
admin.site.register(Preface)
admin.site.register(Score)
