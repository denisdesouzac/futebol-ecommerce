from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView 


urlpatterns = [
    path('', views.principal, name='home'),
    path('loja/', views.loja, name='loja'),
    path('produto/<int:id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('sobre/', views.sobre, name='sobre'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('editar-conta/', views.editar_conta_view, name='editar_conta'),
    path('carrinho/', views.cart_view, name='carrinho'),
    path('logout/', views.custom_logout, name='logout'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_success/', TemplateView.as_view(template_name="order_success.html"), name='order_success'),
    path('pedido/<int:id>/', views.order_detail, name='order_detail'),

    
]
