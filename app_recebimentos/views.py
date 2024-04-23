from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def recebimentos_views(request):
    return render(request, 'pages/recebimentos.html', context={
        'title': 'Recebimentos',
    })