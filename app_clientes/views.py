from django.shortcuts import render

def clientes_views(resquest):
    return render (resquest, 'pages/clientes.html', context= {
        'title': 'Clientes'
    })
