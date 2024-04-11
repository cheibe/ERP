from django.shortcuts import render

def fornecedores_view(request):
    return render(request, 'pages/fornecedores.html', context={
        'title': 'Fornecedores'
    })