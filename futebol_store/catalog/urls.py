from django.urls import path
from . import views

urlpatterns = [
    path('some_url/', views.some_view, name='some_view'),
]

