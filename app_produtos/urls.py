from django.urls import path
from app_produtos import views

app_name = 'produtos'

urlpatterns = [
    path('', views.produtos_view, name='produtos'),
    path('/adicionar', views.adicionar_produtos, name='adicionar_produtos'),
    path('/editar/<produto_id>', views.editar_produto, name='editar_produto'),
    path('/deletar/<produto_id>', views.deletar_produto, name='deletar_produto'),
]
