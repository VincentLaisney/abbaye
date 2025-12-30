from django.contrib import admin
from .models import Personne, Chambre, Sejour, Parloir, Mail, Telephone, Adresse, Retreat

admin.site.register(Personne)
admin.site.register(Chambre)
admin.site.register(Sejour)
admin.site.register(Parloir)
admin.site.register(Mail)
admin.site.register(Telephone)
admin.site.register(Adresse)
admin.site.register(Retreat)
