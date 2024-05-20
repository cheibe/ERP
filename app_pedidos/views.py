from django.shortcuts import render
from app_produtos.models import Produtos

def pedidos_view(request):
    return render(request, 'pages/pedidos.html', context={
        'title': 'Pedidos'
    })

def adicionar_pedido(request):
    produtos = Produtos.objects.all()
    return render(request, 'pages/adicionar_pedido.html', context={
        'title': 'Adicionar pedido',
        'produtos': produtos
    })
