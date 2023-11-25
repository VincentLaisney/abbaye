""" apps/imprimerie/urls.py """

from django.urls import path

from . import views_main
from . import views_memo
from . import views_clients
from . import views_papers
from . import views_projects
from . import views_elements

app_name = 'imprimerie'
urlpatterns = [
    path('', views_main.home, name='home'),
    path('memo/', views_memo.memo, name='memo'),
    path('memo/update/', views_memo.memo_update, name='memo_update'),
    path('clients/', views_clients.list, name='clients_list'),
    path('clients/create/', views_clients.create, name='clients_create'),
    path('clients/<int:pk>/', views_clients.details, name='clients_details'),
    path('clients/<int:pk>/update/', views_clients.update, name='clients_update'),
    path('clients/<int:pk>/delete/', views_clients.delete, name='clients_delete'),
    path('papers/', views_papers.list, name='papers_list'),
    path('papers/create/', views_papers.create, name='papers_create'),
    path('papers/<int:pk>/', views_papers.details, name='papers_details'),
    path('papers/<int:pk>/update/', views_papers.update, name='papers_update'),
    path('papers/<int:pk>/delete/', views_papers.delete, name='papers_delete'),
    path('projects/', views_projects.list, name='projects_list'),
    path('projects/create/', views_projects.create, name='projects_create'),
    path('projects/<int:pk>/', views_projects.details, name='projects_details'),
    path('projects/<int:pk>/update/',
         views_projects.update, name='projects_update'),
    path('projects/<int:pk>/delete/',
         views_projects.delete, name='projects_delete'),
    path('elements/', views_elements.list, name='elements_list'),
    path('elements/create/', views_elements.create, name='elements_create'),
    path('elements/<int:pk>/', views_elements.details, name='elements_details'),
    path('elements/<int:pk>/update/',
         views_elements.update, name='elements_update'),
    path('elements/<int:pk>delete/', views_elements.delete, name='elements_delete'),
]
