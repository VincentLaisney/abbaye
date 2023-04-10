""" apps/agenda/urls.py """

from django.urls import path

from . import views

app_name = 'agenda'
urlpatterns = [
    path('list/', views.agenda_as_list, name='list'),
    path('calendar/', views.agenda_as_calendar, name='calendar'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.details, name='details'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
