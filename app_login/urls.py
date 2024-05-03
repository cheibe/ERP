from django.urls import path
from app_login import views

app_name='login'

urlpatterns = [
    path('', views.login, name='login'),
]
