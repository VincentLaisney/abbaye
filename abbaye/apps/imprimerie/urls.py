""" apps/imprimerie/urls.py """

from django.urls import path

from . import views_main
from . import views_work
from . import views_memo
from . import views_clients
from . import views_papers
from . import views_projects
from . import views_elements

app_name = 'imprimerie'
urlpatterns = [
    path('', views_main.home, name='home'),
    # Work:
    path('work/', views_work.work, name='work'),
    path('work/update/', views_work.work_update, name='work_update'),
    # Memo:
    path('memo/', views_memo.memo, name='memo'),
    path('memo/update/', views_memo.memo_update, name='memo_update'),
    # Clients:
    path('clients/', views_clients.list, name='clients_list'),
    path('clients/create/', views_clients.create, name='client_create'),
    path('clients/<int:pk>/', views_clients.details, name='client_details'),
    path('clients/<int:pk>/update/', views_clients.update, name='client_update'),
    path('clients/<int:pk>/delete/', views_clients.delete, name='client_delete'),
    path(
        'clients/autocomplete/',
        views_clients.ClientAutocompleteView.as_view(),
        name='clients_autocomplete'
    ),
    # Papers:
    path('papers/', views_papers.list, name='papers_list'),
    path('papers/create/', views_papers.create, name='paper_create'),
    path('papers/<int:pk>/', views_papers.details, name='paper_details'),
    path('papers/<int:pk>/update/', views_papers.update, name='paper_update'),
    path('papers/<int:pk>/delete/', views_papers.delete, name='paper_delete'),
    path('papers/autocomplete/',
         views_papers.PaperAutocompleteView.as_view(),
         name='papers_autocomplete'),
    path('papers/fetch_paper_data/<int:id_paper>/',
         views_papers.fetch_paper_data),
    # Projects:
    path('projects/', views_projects.list, name='projects_list'),
    path('projects/create/', views_projects.create, name='project_create'),
    path('projects/<int:pk>/', views_projects.details, name='project_details'),
    path('projects/<int:pk>/update/',
         views_projects.update, name='project_update'),
    path('projects/<int:pk>/delete/',
         views_projects.delete, name='project_delete'),
    # Elements:
    path('projects/<int:pk_project>/element_create/',
         views_elements.create, name='element_create'),
    path('projects/<int:pk_project>/element_details/<int:pk>/',
         views_elements.details, name='element_details'),
    path('projects/<int:pk_project>/element_update/<int:pk>/',
         views_elements.update, name='element_update'),
    path('projects/<int:pk_project>/element_delete/<int:pk>',
         views_elements.delete, name='element_delete')
]
