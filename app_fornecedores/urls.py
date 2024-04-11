from django.urls import path
from app_fornecedores import views

app_name = 'fornecedores'

urlpatterns = [
    path('', views.fornecedores_view, name='fornecedores'),
]
