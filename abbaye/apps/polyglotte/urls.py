""" apps/polyglotte/urls.py """

from django.urls import path

from . import views

app_name = 'polyglotte'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:book>/<int:chapter>/', views.verses_list, name='list'),
    path('<str:book>/<int:chapter>/<int:verse>',
         views.verse_update, name='update'),
    path('search/', views.search, name='search'),
]
