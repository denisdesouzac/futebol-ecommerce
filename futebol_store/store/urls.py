from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('loja/', views.loja, name='loja'),
    path('sobre/', views.sobre, name='sobre'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home_view, name='home'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('editar-conta/', views.editar_conta_view, name='editar_conta'),
    path('carrinho/', views.carrinho_view, name='carrinho'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
