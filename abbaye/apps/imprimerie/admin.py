""" apps/imprimerie/admin.py """

from django.contrib import admin
from .models import Memo, Client, Paper, Project, Element

admin.site.register(Memo)
admin.site.register(Client)
admin.site.register(Paper)
admin.site.register(Project)
admin.site.register(Element)
