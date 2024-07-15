from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('loja', views.loja, name='loja'),
    path('sobre', views.sobre, name='sobre'),
]