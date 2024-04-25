from django.urls import path
from app_empresas import views

app_name = 'empresas'

urlpatterns = [
    path('', views.empresas_view, name='empresas'),
    path('adicionar/', views.adicionar_empresa, name='adicionar_empresa'),
    path('editar/<empresa_id>', views.editar_empresa, name='editar_empresa'),
    path('deletar/<empresa_id>', views.deletar_empresa, name='deletar_empresa')
]
