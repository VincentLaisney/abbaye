""" apps/editor/urls.py """

from django.urls import path

from . import views_main
from . import views_books
from . import views_disks
from . import views_images


app_name = 'editor'
urlpatterns = [
    path('', views_main.home, name='home'),

    # Books:
    path('books/', views_books.books_list, name='books_list'),
    path('books/create/', views_books.book_create, name='book_create'),
    path('books/<int:pk>/', views_books.book_details, name='book_details'),
    path('books/<int:pk>/update/', views_books.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views_books.book_delete, name='book_delete'),

    # Disks:
    path('disks/', views_disks.disks_list, name='disks_list'),
    path('disks/create/', views_disks.disk_create, name='disk_create'),
    path('disks/<int:pk>/', views_disks.disk_details, name='disk_details'),
    path('disks/<int:pk>/update/', views_disks.disk_update, name='disk_update'),
    path('disks/<int:pk>/delete/', views_disks.disk_delete, name='disk_delete'),

    # Images:
    path('images/', views_images.images_list, name='images_list'),
    path('images/create/', views_images.image_create, name='image_create'),
    path('images/<int:pk>/', views_images.image_details, name='image_details'),
    path('images/<int:pk>/update/', views_images.image_update, name='image_update'),
    path('images/<int:pk>/delete/', views_images.image_delete, name='image_delete'),
]
