from django.urls import path
from app_recebimentos import views

app_name = 'recebimentos'

urlpatterns = [
    path('', views.recebimentos_views, name='recebimentos'),
]
