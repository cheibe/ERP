from django.shortcuts import render, redirect, get_object_or_404
from app_fornecedores.models import Fornecedor
from app_fornecedores.forms import FornecedorForm, EditFornecedorForm

def fornecedores_view(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'pages/fornecedores.html', context={
        'title': 'Fornecedores',
        'fornecedores': fornecedores
    })