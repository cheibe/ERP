from django.shortcuts import render, redirect, get_object_or_404
from app_produtos.models import Produtos
from app_produtos.forms import ProdutosForm, EditProdutosForm
from django.contrib import messages

def produtos_view(request):
    produtos = Produtos.objects.all()
    return render(request, 'pages/produtos.html', context={
        'title': 'Pordutos',
        'produtos': produtos,
    })

def adicionar_produtos(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST)
        if form.is_valid():
            novo_produto = form.save()
            messages.success(request, f'O produto "{novo_produto.nome}" foi adicionado com sucesso!')
            return redirect ('produtos:produtos')
    else:
        form = ProdutosForm()

    return render (request, 'pages/adicionar_produto.html', context={
        'title': 'Adicionar produtos',
        'form': form
    })

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

def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produtos, pk=produto_id)
    
    produto.delete()
    messages.success(request, "O produto foi deletado com sucesso!")
    return redirect ('produtos:produtos')