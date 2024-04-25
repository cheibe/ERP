from django.shortcuts import render

def usuarios_view(request):
    return render(request, 'pages/usuarios.html', context={
        'title': 'Usuários'
    })
