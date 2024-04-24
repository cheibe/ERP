from django.shortcuts import render

def empresas_view(request):
    return render(request, 'pages/empresas.html', context={
        'title': 'Empresas'
    })