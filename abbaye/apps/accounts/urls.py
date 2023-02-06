""" apps/accounts/urls.py """

from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.AbbayeLoginView.as_view(), name='login'),
    path('login_group_required/', views.AbbayeLoginGroupRequiredView.as_view(),
         name='login_group_required'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
