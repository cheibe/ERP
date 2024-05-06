from django.shortcuts import render, redirect, get_object_or_404
from app_fornecedores.models import Fornecedor
from app_fornecedores.forms import FornecedorForm, EditFornecedorForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login:login', redirect_field_name='next')
def fornecedores_view(request):
    if request.user.is_staff:
        fornecedores = Fornecedor.objects.all()
    else:
        fornecedores = Fornecedor.objects.filter(empresa=request.user.empresa)
    return render(request, 'pages/fornecedores.html', context={
        'title': 'Fornecedores',
        'fornecedores': fornecedores
    })

@login_required(login_url='login:login', redirect_field_name='next')
def adicionar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request, request.POST)
        if form.is_valid():
            novo_fornecedor = form.save(commit=False)
            novo_fornecedor.empresa = form.cleaned_data.get('empresa', request.user.empresa)
            form.save()
            messages.success(request, f'O fornecedor "{novo_fornecedor.nome}" foi adicionado com sucesso!')
            return redirect ('fornecedores:fornecedores')
    else:
        form = FornecedorForm(request)

    return render (request, 'pages/adicionar_fornecedor.html', context={
        'title': 'Adicionar fornecedor',
        'form': form
    })

@login_required(login_url='login:login', redirect_field_name='next')
def editar_fornecedor(request, fornecedor_id):
    fornecedor = get_object_or_404(Fornecedor, pk=fornecedor_id)
    if request.method == 'POST':
        form = EditFornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            fornecedor_edit = form.save()
            messages.success(request, f'O fornecedor "{fornecedor_edit.nome}" foi editado com sucesso!')
            return redirect('fornecedores:fornecedores')
    else:
        form = EditFornecedorForm(instance=fornecedor)

    return render (request, 'pages/adicionar_fornecedor.html', context={
        'title': 'Editar fornecedor',
        'form': form
    })

@login_required(login_url='login:login', redirect_field_name='next')
def delete_fornecedor(request, fornecedor_id):
    fornecedor = get_object_or_404(Fornecedor, pk=fornecedor_id)
    
    fornecedor.delete()
    messages.success(request, f'O fornecedor foi deletado com sucesso!')
    return redirect('fornecedores:fornecedores')