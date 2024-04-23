from django.shortcuts import render

def recebimentos_views(request):
    return render(request, 'pages/recebimentos.html', context={
        'title': 'Recebimentos',
    })