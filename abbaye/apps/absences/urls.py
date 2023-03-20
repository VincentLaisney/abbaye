""" apps/absences/urls.py """

from django.urls import path

from . import views

app_name = 'absences'
urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.success, name='success'),
    path('failure/', views.failure, name='failure'),
    path('create/', views.create, name='create'),
    path('<pk>', views.details, name='details'),
    path('<pk>/update/', views.update, name='update'),
    path('<pk>/delete/', views.delete, name='delete'),
]
