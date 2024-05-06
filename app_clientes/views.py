from django.shortcuts import render, redirect, get_object_or_404
from app_clientes.models import Cliente
from app_clientes.forms import ClienteForm, EditClienteForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login:login', redirect_field_name='next')
def clientes_views(resquest):
    if resquest.user.is_staff:
        clientes = Cliente.objects.all()
    else:
        clientes = Cliente.objects.filter(empresa=resquest.user.empresa)
    return render (resquest, 'pages/clientes.html', context= {
        'title': 'Clientes',
        'clientes': clientes,
    })

@login_required(login_url='login:login', redirect_field_name='next')
def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request, request.POST)
        if form.is_valid():
            novo_cliente = form.save(commit=False)
            novo_cliente.empresa = form.cleaned_data.get('empresa', request.user.empresa)
            messages.success(request, f"O cliente '{novo_cliente.razao_social}' foi cadastrado com sucesso!")
            form.save()
            return redirect ('clientes:clientes')
    else:
        form = ClienteForm(request)

    return render (request, 'pages/adicionar_cliente.html', context= {
        'title': 'Adicionar cliente',
        'form': form,
    })

@login_required(login_url='login:login', redirect_field_name='next')
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    if request.method == 'POST':
        form = EditClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            edit_cliente = form.save()
            messages.success(request, f"O cliente '{edit_cliente.razao_social}' foi editado com sucesso!")
            return redirect ('clientes:clientes')
    else:
        form = EditClienteForm(instance=cliente)
    
    return render (request, 'pages/adcionar_cliente.html', context={
        'title': 'Editar cliente',
        'form': form
    })

@login_required(login_url='login:login', redirect_field_name='next')
def deletar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    cliente.delete()
    messages.success(request, 'O cliente foi deletado com sucesso!')
    return redirect('clientes:clientes')
    