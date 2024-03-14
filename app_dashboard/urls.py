from django.urls import path
from app_dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home_view, name='home')
]
