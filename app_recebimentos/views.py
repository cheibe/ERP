from django.shortcuts import render, redirect, get_object_or_404
from app_recebimentos.models import Recebimento
from app_recebimentos.forms import RecebimentoForm, EditRecebimentoForm 
from django.contrib import messages
from app_recebimentos.tables import RecebimentoTable
from django.contrib.auth.decorators import login_required

@login_required(login_url='login:login', redirect_field_name='next')
def recebimentos_views(request):
    if request.user.is_staff:
        recebimentos = Recebimento.objects.all()
    else:
        recebimentos = Recebimento.objects.filter(empresa=request.user.empresa)
    table = RecebimentoTable(recebimentos)
    return render(request, 'pages/recebimentos.html', context={
        'title': 'Recebimentos',
        'table': table
    })

@login_required(login_url='login:login', redirect_field_name='next')
def adicionar_recebimento(request):
    if request.method == 'POST':
        form = RecebimentoForm(request, request.POST)
        if form.is_valid():
            novo_recebimento = form.save(commit=False)
            novo_recebimento.empresa = form.cleaned_data.get('empresa', request.user.empresa)
            form.save()
            messages.success(request, f'O recebimento do cliente "{novo_recebimento.cliente.razao_social}" foi adicionado com sucesso! ')
            return redirect('recebimentos:recebimentos')
    else:
        form = RecebimentoForm(request)
        
    return render(request, 'pages/adicionar_recebimento.html', context={
        'title': 'Adicionar recebimentos',
        'form': form
    })

@login_required(login_url='login:login', redirect_field_name='next')
def editar_recebimento(request, recebimento_id):
    recebimento = get_object_or_404(Recebimento, pk=recebimento_id)
    if request.method == 'POST':
        form = EditRecebimentoForm(request.POST, instance=recebimento)
        if form.is_valid():
            edit_recebimento = form.save()
            messages.success(request, f'O recebimento do cliente "{edit_recebimento.client.razao_social}" foi editado com sucesso!')
            return redirect('recebimentos:recebimentos')
    else:
        form = EditRecebimentoForm(instance=recebimento)

    return render(request, 'pages/adicionar_recebimento.html', context={
        'title': 'Editar recebimento',
        'form': form
    })

@login_required(login_url='login:login', redirect_field_name='next')
def delete_recebimento(request, recebimento_id):
    recebimento = get_object_or_404(Recebimento, pk=recebimento_id)

    recebimento.delete()
    messages.success(request, f'O recebimento foi deletado com sucesso!')
    return redirect('recebimentos:recebimentos')