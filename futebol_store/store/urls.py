from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('loja/', views.loja, name='loja'),  # Note a barra no final
    path('sobre/', views.sobre, name='sobre'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home_view, name='home'),
]
