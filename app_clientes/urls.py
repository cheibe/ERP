from django.urls import path
from app_clientes import views

app_name = 'clientes'

urlpatterns = [
    path('', views.clientes_views, name='clientes'),
]
