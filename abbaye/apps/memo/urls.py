""" apps/memo/urls.py """

from django.urls import path

from . import views

app_name = 'memo'
urlpatterns = [
    path('', views.home, name='home'),
    path('install/', views.install, name='install'),
    path('commands/', views.commands, name='commands'),
    path('sh/', views.sh, name='sh'),
    path('py/', views.py, name='py'),
    path('js/', views.js, name='js'),
    path('mysql/', views.mysql, name='mysql'),
    path('vim/', views.vim, name='vim'),
    path('git/', views.git, name='git'),
]
