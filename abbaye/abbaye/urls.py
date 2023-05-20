""" abbaye/urls.py """

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('abbaye/', include('apps.main.urls')),
    path('abbaye/admin/', admin.site.urls),
    path('abbaye/accounts/', include('apps.accounts.urls')),
    path('abbaye/absences/', include('apps.absences.urls')),
    path('abbaye/accenteur/', include('apps.accenteur.urls')),
    path('abbaye/agenda/', include('apps.agenda.urls')),
    path('abbaye/barcode/', include('apps.barcode.urls')),
    path('abbaye/courses/', include('apps.courses.urls')),
    path('abbaye/editor/', include('apps.editor.urls')),
    path('abbaye/hotellerie/', include('apps.hotellerie.urls')),
    path('abbaye/imprimerie/', include('apps.imprimerie.urls')),
    path('abbaye/infirmerie/', include('apps.infirmerie.urls')),
    path('abbaye/jgabc/', include('apps.jgabc.urls')),
    path('abbaye/livrets/', include('apps.livrets.urls')),
    path('abbaye/memo/', include('apps.memo.urls')),
    path('abbaye/moines/', include('apps.moines.urls')),
    path('abbaye/ordomatic/', include('apps.ordomatic.urls')),
    path('abbaye/ornitho/', include('apps.ornitho.urls')),
    path('abbaye/polyglotte/', include('apps.polyglotte.urls')),
    path('abbaye/typetrainer/', include('apps.typetrainer.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
