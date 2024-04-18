from django.urls import path
from app_pagamentos import views

app_name = 'pagamentos'

urlpatterns = [
    path('', views.pagamentos_views, name='pagamentos'),
]
