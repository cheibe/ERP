from django.urls import path
from app_produtos import views

app_name = 'produtos'

urlpatterns = [
    path('', views.produtos_view, name='produtos'),
]
