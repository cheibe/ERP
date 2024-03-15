from django.shortcuts import render

def produtos_view(request):
    return render(request, 'pages/produtos.html', context={
        'title': 'Pordutos'
    })