from django.shortcuts import render

def pedidos_view(request):
    return render(request, 'pages/pedidos.html', context={
        'title': 'Pedidos'
    })
