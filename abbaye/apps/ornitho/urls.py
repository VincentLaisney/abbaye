""" apps/ornitho/urls.py """

from django.urls import path

from . import views

app_name = 'ornitho'
urlpatterns = [
    path('', views.home, name='home'),
    path('list/<str:category>/', views.list, name='list'),
    path('list/', views.list, name='list'),
    path('galleria/', views.galleria, name='galleria'),
    # path('create/', views.create, name='create'),
    # path('<int:pk>/', views.details, name='details'),
    # path('<int:pk>/update/', views.update, name='update'),
    # path('<int:pk>/delete/', views.delete, name='delete'),
]
