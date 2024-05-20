from django.shortcuts import render, redirect, get_object_or_404
from app_produtos.models import Produtos
from app_produtos.forms import ProdutosForm, EditProdutosForm
from app_produtos.tables import ProdutosTable
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login:login', redirect_field_name='next')
def produtos_view(request):
    if request.user.is_staff:
        produtos = Produtos.objects.all()
    else:
        produtos = Produtos.objects.filter(empresa=request.user.empresa)
    table = ProdutosTable(produtos)
    return render(request, 'pages/produtos.html', context={
        'title': 'Pordutos',
        'table': table,
    })

@login_required(login_url='login:login', redirect_field_name='next')
def adicionar_produtos(request):
    if request.method == 'POST':
        form = ProdutosForm(request, request.POST)
        if form.is_valid():
            novo_produto = form.save(commit=False)
            novo_produto.empresa = form.cleaned_data.get('empresa', request.user.empresa)
            form.save()
            messages.success(request, f'O produto "{novo_produto.nome}" foi adicionado com sucesso!')
            return redirect ('produtos:produtos')
    else:
        form = ProdutosForm(request)

    return render (request, 'pages/adicionar_produto.html', context={
        'title': 'Adicionar produtos',
        'form': form
    })

@login_required(login_url='login:login', redirect_field_name='next')
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produtos, pk=produto_id)
    if request.method == 'POST':
        form = EditProdutosForm(request.POST, instance=produto)
        if form.is_valid():
            porduto_edit = form.save()
            messages.success(request, f'O produto "{porduto_edit.nome}" foi editado com sucesso!')
            return redirect('produtos:produtos')
    else:
        form = EditProdutosForm(instance=produto)

    return render (request, 'pages/adicionar_produto.html', context={
        'title': 'Editar produto',
        'form': form
    })

@login_required(login_url='login:login', redirect_field_name='next')
def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produtos, pk=produto_id)
    
    produto.delete()
    messages.success(request, "O produto foi deletado com sucesso!")
    return redirect ('produtos:produtos')