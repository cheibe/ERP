from django.shortcuts import render, redirect, get_object_or_404
from app_pagamentos.models import Pagamento
from app_pagamentos.forms import PagamentoForm, EditPagamentoForm
from django.contrib import messages
from app_pagamentos.tables import PagamentoTable

def pagamentos_views(request):
    pagamentos = Pagamento.objects.all()
    table = PagamentoTable(pagamentos)
    return render(request, 'pages/pagamentos.html', context={
        'title': 'Pagamentos',
        'table': table
    })

def adicionar_pagamento(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            novo_pagamento = form.save()
            messages.success(request, f'O pagamento do fornecedor "{novo_pagamento.fornecedor.nome}" foi adicionado com sucesso!')
            return redirect('pagamentos:pagamentos')
    else:
        form = PagamentoForm()

    return render(request, 'pages/adicionar_pagamento.html', context={
        'title': 'Adicionar pagamento',
        'form': form, 
    })

def editar_pagamento(request, pagamento_id):
    pagamento = get_object_or_404(Pagamento, pk=pagamento_id)
    if request.method == 'POST':
        form = EditPagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            pagamento_edit = form.save()
            messages.success(request, f'O pagamento do fornecedor "{pagamento_edit.fornecedor.nome}" foi editado com sucesso!')
            return redirect('pagamentos:pagamentos')
    else:
        form = EditPagamentoForm(instance=pagamento)

    return render(request, 'pages/adicionar_pagamento.html', context={
        'title': 'Editar pagamento',
        'form': form,
        'pagamento': pagamento
    })

def delete_pagamento(request, pagamento_id):
    pagamento = get_object_or_404(Pagamento, pk=pagamento_id)

    pagamento.delete()
    messages.success(request, 'O pagamento foi deletado com sucesso!')
    return redirect('pagamentos:pagamentos')