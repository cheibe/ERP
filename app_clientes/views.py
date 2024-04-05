from django.shortcuts import render, redirect, get_object_or_404
from app_clientes.models import Cliente
from app_clientes.forms import ClienteForm, EditClienteForm
from django.contrib import messages

def clientes_views(resquest):
    cliente = Cliente.objects.all()

    return render (resquest, 'pages/clientes.html', context= {
        'title': 'Clientes',
        'cliente': cliente,
    })

def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            novo_cliente = form.save()
            messages.success(f"O cliente '{novo_cliente.nome}' foi cadastrado com sucesso!")
            return redirect ('clientes:clientes')
    else:
        form = ClienteForm()

    return render (request, 'pages/adicionar_cliente.html', context= {
        'title': 'Adicionar cliente',
        'form': form,
    })

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    if request.method == 'POST':
        form = EditClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            edit_cliente = form.save()
            messages.success(f"O cliente '{edit_cliente.nome}' foi editado com sucesso!")
            return redirect ('clientes:clientes')
    else:
        form = EditClienteForm(instance=cliente)
    
    return render (request, 'pages/adcionar_cliente.html', context={
        'title': 'Editar cliente',
        'form': form
    })

def deletar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    cliente.delete()
    messages.success('O cliente foi deletado com sucesso!')
    return redirect('clientes:clientes')
    