from django.urls import path
from app_pedidos import views

app_name = 'pedidos'

urlpatterns = [
    path('', views.pedidos_view, name='pedidos'),
    path('adicionar/', views.adicionar_pedido, name='adicionar_pedido')
]
