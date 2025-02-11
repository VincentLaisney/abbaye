""" apps/infirmerie/urls.py """

from django.urls import path, re_path

from . import views

app_name = 'infirmerie'
urlpatterns = [
    # Home:
    path('', views.home, name='home'),

    # Toubibs:
    re_path(r'^(search=(?P<search>\w+)/)?page=(?P<page>\d+)$',
            views.ToubibListView.as_view(), name='list'),
    path('repertoire/<letter>', views.toubibs_repertoire, name='repertoire'),
    path('create', views.ToubibCreateView.as_view(), name='create'),
    path('id=<int:pk>/detail', views.ToubibDetailView.as_view(), name='detail'),
    path('id=<int:pk>/update', views.ToubibUpdateView.as_view(), name='update'),
    path('id=<int:pk>/delete', views.ToubibDeleteView.as_view(), name='delete'),
    path('autocomplete/',
         views.ToubibAutocompleteView.as_view(), name='autocomplete'),

    # Specialities:
    path('specialities/list', views.specialities_list, name='specialities_list'),
    path('specialities/create', views.specialities_create,
         name='specialities_create'),
    path('specialities/<int:pk>/update',
         views.specialities_update, name='specialities_update'),
    path('specialities/<int:pk>/delete',
         views.specialities_delete, name='specialities_delete'),

    # Billets:
    path('', views.HomeView.as_view(), name='home'),
    re_path(r'^agenda/(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})/$',
            views.AgendaView.as_view(), name='agenda'),
    path('list/', views.billets_list_view, name='list'),
    path('list/page=<int:page>', views.billets_list_view, name='list_page'),
    path('create', views.BilletCreateView.as_view(), name='create'),
    path('id=<int:pk>/detail', views.BilletDetailView.as_view(), name='detail'),
    path('id=<int:pk>/update', views.BilletUpdateView.as_view(), name='update'),
    path('id=<int:pk>/delete', views.BilletDeleteView.as_view(), name='delete'),
    path('id=<int:pk>/pdf', views.BilletPDFView.as_view(), name='pdf'),
]
