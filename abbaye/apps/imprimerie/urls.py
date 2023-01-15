""" apps/imprimerie/urls.py """

from django.urls import path

from . import views

app_name = 'imprimerie'
urlpatterns = [
    path('', views.home, name='home'),
    path('memo', views.memo, name='memo'),
    path('memo/update', views.memo_update, name='memo_update'),
]
