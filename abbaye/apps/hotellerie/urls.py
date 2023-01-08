""" apps/hotellerie/urls.py """

from django.urls import path, re_path

from . import views_main
from . import views_personnes
from . import views_sejours
from . import views_parloirs
from . import views_retraites
from . import views_listings

app_name = 'hotellerie'
urlpatterns = [
    path('', views_main.home, name='main_home'),
    path('calendar/', views_main.calendar, name='main_calendar'),
    re_path(r'^calendar/(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})/$',
            views_main.calendar, name='main_calendar'),

    path('personnes/list/<str:letter>/',
         views_personnes.list, name='personnes_list'),
    path('personnes/list/<str:letter>/<str:search>/',
         views_personnes.list, name='personnes_list'),
    path('personnes/create/', views_personnes.create, name='personnes_create'),
    path('personnes/<int:pk>/', views_personnes.details, name='personnes_details'),
    path('personnes/<int:pk>/update/',
         views_personnes.update, name='personnes_update'),
    path('personnes/<int:pk>/delete/',
         views_personnes.delete, name='personnes_delete'),
    path('personnes/get_pere_suiveur/',
         views_personnes.get_pere_suiveur, name='personnes_get_pere_suiveur'),
    path(
        'personnes/autocomplete_hotes/',
        views_personnes.PersonneAutocompleteHotesView.as_view(),
        name='personnes_autocomplete_hotes'
    ),
    path(
        'personnes/autocomplete_monks/',
        views_personnes.PersonneAutocompleteMonksView.as_view(),
        name='personnes_autocomplete_monks'
    ),

    path('sejours/list/', views_sejours.list, name='sejours_list'),
    path('sejours/create/', views_sejours.create, name='sejours_create'),
    path('sejours/<int:pk>/', views_sejours.details, name='sejours_details'),
    path('sejours/<int:pk>/update/', views_sejours.update, name='sejours_update'),
    path('sejours/<int:pk>/delete/', views_sejours.delete, name='sejours_delete'),
    path('sejours/rooms/', views_sejours.get_rooms_status, name='sejours_rooms'),

    path('parloirs/list/', views_parloirs.list, name='parloirs_list'),
    path('parloirs/create/', views_parloirs.create, name='parloirs_create'),
    path('parloirs/<int:pk>/', views_parloirs.details, name='parloirs_details'),
    path('parloirs/<int:pk>/update/',
         views_parloirs.update, name='parloirs_update'),
    path('parloirs/<int:pk>/delete/',
         views_parloirs.delete, name='parloirs_delete'),

    path('retreats/list/', views_retraites.list, name='retreats_list'),
    path('retreats/create/', views_retraites.create, name='retreats_create'),
    path('retreats/<int:pk>/', views_retraites.details, name='retreats_details'),
    path('retreats/<int:pk>/update/',
         views_retraites.update, name='retreats_update'),
    path('retreats/<int:pk>/delete/',
         views_retraites.delete, name='retreats_delete'),

    path('listings/cuisine/', views_listings.cuisine, name='listings_cuisine'),
    path('listings/hotellerie/', views_listings.hotellerie,
         name='listings_hotellerie'),
]
