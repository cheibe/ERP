from django.urls import path
from app_usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.usuarios_view, name='usuarios'),
]
