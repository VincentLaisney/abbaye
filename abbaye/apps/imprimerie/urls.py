""" apps/imprimerie/urls.py """

from django.urls import path

from . import views

app_name = 'imprimerie'
urlpatterns = [
    path('', views.home, name='home'),
    path('memo', views.memo, name='memo'),
    path('memo/update', views.memo_update, name='memo_update'),
    path('clients/', views.clients_list, name='clients_list'),
    path('client/create', views.client_create, name='client_create'),
    path('client/details', views.client_details, name='client_details'),
    path('client/update', views.client_update, name='client_update'),
    path('client/delete', views.client_delete, name='client_delete'),
    path('papers/', views.papers_list, name='papers_list'),
    path('paper/create', views.paper_create, name='paper_create'),
    path('paper/details', views.paper_details, name='paper_details'),
    path('paper/update', views.paper_update, name='paper_update'),
    path('paper/delete', views.paper_delete, name='paper_delete'),
    path('jobs/', views.jobs_list, name='jobs_list'),
    path('job/create', views.job_create, name='job_create'),
    path('job/details', views.job_details, name='job_details'),
    path('job/update', views.job_update, name='job_update'),
    path('job/delete', views.job_delete, name='job_delete'),
    path('elements/', views.elements_list, name='elements_list'),
    path('element/create', views.element_create, name='element_create'),
    path('element/details', views.element_details, name='element_details'),
    path('element/update', views.element_update, name='element_update'),
    path('element/delete', views.element_delete, name='element_delete'),
]
