from app_empresas.models import Empresa
from app_empresas.forms import EmpresaForm, EditEmpresaForm
from django.shortcuts import render, redirect, get_object_or_404
from app_empresas.tables import EmpresaTable
from django.contrib import messages

def empresas_view(request):
    empresas = Empresa.objects.all()
    table = EmpresaTable(empresas)
    return render(request, 'pages/empresas.html', context={
        'title': 'Empresas',
        'table': table
    })

def adicionar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            nova_empresa = form.save()
            messages.success(request, f'A empresa "{nova_empresa.nome_fantasia}" foi cadastrada com sucesso! ')
            return redirect('empresas:empresas')
    else:
        form = EmpresaForm()
    return render(request, 'pages/adicionar_empresa.html', context={
        'title': 'Adcionar empresa',
        'form': form
    })

def editar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    if request.method == 'POST':
        form = EditEmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            edit_empresa = form.save()
            messages.success(request, f'A empresa "{edit_empresa.nome_fantasia}" foi editada com sucesso!')
            return redirect('empresas:empresas')
    else:
        form = EditEmpresaForm(instance=empresa)
    return render(request, 'pages/adicionar_empresa.html', context={
        'title': 'Editar empresa',
        'form': form
    })

def deletar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)

    empresa.delete()
    messages.success(request, f'A empresa foi deletada com sucesso!')
    return redirect('empresas:empresas')