""" abbaye/urls.py """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('apps.main.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('summernote/', include('django_summernote.urls')),

    path('absences/', include('apps.absences.urls')),
    path('accenteur/', include('apps.accenteur.urls')),
    path('agenda/', include('apps.agenda.urls')),
    path('barcode/', include('apps.barcode.urls')),
    path('courses/', include('apps.courses.urls')),
    path('editor/', include('apps.editor.urls')),
    path('hotellerie/', include('apps.hotellerie.urls')),
    path('imprimerie/', include('apps.imprimerie.urls')),
    path('infirmerie/', include('apps.infirmerie.urls')),
    path('jgabc/', include('apps.jgabc.urls')),
    path('livrets/', include('apps.livrets.urls')),
    path('memo/', include('apps.memo.urls')),
    path('moines/', include('apps.moines.urls')),
    path('ordomatic/', include('apps.ordomatic.urls')),
    path('ornitho/', include('apps.ornitho.urls')),
    path('polyglotte/', include('apps.polyglotte.urls')),
    path('typetrainer/', include('apps.typetrainer.urls')),
]
