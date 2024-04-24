from django.shortcuts import render, redirect, get_object_or_404
from app_recebimentos.models import Recebimento
from app_recebimentos.forms import RecebimentoForm, EditRecebimentoForm 
from django.contrib import messages
from app_recebimentos.tables import RecebimentoTable

def recebimentos_views(request):
    recebimentos = Recebimento.objects.all()
    table = RecebimentoTable(recebimentos)
    return render(request, 'pages/recebimentos.html', context={
        'title': 'Recebimentos',
        'table': table
    })

def adicionar_recebimento(request):
    if request.method == 'POST':
        form = RecebimentoForm(request.POST)
        if form.is_valid():
            novo_recebimento = form.save()
            messages.success(request, f'O recebimento do cliente "{novo_recebimento.cliente.razao_social}" foi adicionado com sucesso! ')
            return redirect('recebimentos:recebimentos')
    else:
        form = RecebimentoForm()
        
    return render(request, 'pages/adicionar_recebimento.html', context={
        'title': 'Adicionar recebimentos',
        'form': form
    })

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

def delete_recebimento(request, recebimento_id):
    recebimento = get_object_or_404(Recebimento, pk=recebimento_id)

    recebimento.delete()
    messages.success(request, f'O recebimento foi deletado com sucesso!')
    return redirect('recebimentos:recebimentos')