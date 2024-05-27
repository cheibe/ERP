from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('produtos/list', views.produtos_api_list, name='produto_api')
]
