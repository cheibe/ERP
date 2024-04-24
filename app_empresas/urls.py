from django.urls import path
from app_empresas import views

app_name = 'empresas'

urlpatterns = [
    path('', views.empresas_view, name='empresas')
]
