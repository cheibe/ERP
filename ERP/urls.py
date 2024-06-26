from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_dashboard.urls')),
    path('produtos/', include('app_produtos.urls')),
    path('clientes/', include('app_clientes.urls')),
    path('fornecedores/', include('app_fornecedores.urls')),
    path('pagamentos/', include('app_pagamentos.urls')),
    path('recebimentos/', include('app_recebimentos.urls')),
    path('empresas/', include('app_empresas.urls')),
    path('usuarios/', include('app_usuarios.urls')),
    path('login/', include('app_login.urls')),
    path('pedidos/', include('app_pedidos.urls')),
    path('api/', include('api.urls'))
]
