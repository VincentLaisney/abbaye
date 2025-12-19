""" apps/livrets/admin.py """

from django.contrib import admin
from .models import Day, BMV, Preface, Score

#admin.site.register(Day)
@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ['ref', 'title', 'rang', 'precedence']
    list_filter = ['precedence']
    search_fields = ['ref']

admin.site.register(BMV)
admin.site.register(Preface)

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ['type', 'ref', 'name', 'page']
    list_filter = ['type']
    search_fields = ['ref']

