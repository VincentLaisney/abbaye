""" apps/ornitho/urls.py """

from django.urls import path

from . import views

app_name = 'ornitho'
urlpatterns = [
    path('', views.home, name='home'),
    path('list/<str:category>/', views.list, name='list'),
    path('list/', views.list, name='list'),
    path('galerie/', views.galerie, name='galerie'),
    path('galerie-paysages/', views.galerie_paysages, name='galerie-paysages'),
    path('galerie-oiseaux/', views.galerie_oiseaux, name='galerie-oiseaux'),
    path('galerie-mammiferes/', views.galerie_mammiferes,
         name='galerie-mammiferes'),
    path('galerie-insectes/', views.galerie_insectes, name='galerie-insectes'),
    path('galerie-reptiles-amphibiens/', views.galerie_reptiles_amphibiens,
         name='galerie-reptiles-amphibiens'),
    path('galerie-plantes/', views.galerie_plantes, name='galerie-plantes'),
    path('galerie-flavigny/', views.galerie_flavigny, name='galerie-flavigny'),
    # path('create/', views.create, name='create'),
    # path('<int:pk>/', views.details, name='details'),
    # path('<int:pk>/update/', views.update, name='update'),
    # path('<int:pk>/delete/', views.delete, name='delete'),
]
