from django.urls import path
from app_clientes import views

app_name = 'clientes'

urlpatterns = [
    path('', views.clientes_views, name='clientes'),
    path('adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('editar/<cliente_id>', views.editar_cliente, name='editar_cliente'),
    path('deletar/<cliente_id>', views.deletar_cliente, name='deletar_cliente')
]
