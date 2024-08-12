from django.shortcuts import redirect
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.principal, name='home'),
    path('loja/', views.loja, name='loja'),
    path('produto/<int:id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<slug:slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
    path('sobre/', views.sobre, name='sobre'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('editar-conta/', views.editar_conta, name='editar_conta'),
    path('carrinho/', views.cart_view, name='carrinho'),
    path('logout/', views.custom_logout, name='logout'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_success/', TemplateView.as_view(template_name="order_success.html"), name='order_success'),
    path('pedido/<int:id>/', views.order_detail, name='order_detail'),
    path('order-summary/', views.order_summary, name='order-summary'),
]

