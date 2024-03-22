from django.shortcuts import render, redirect, get_object_or_404
from app_produtos.models import Produtos
from app_produtos.forms import ProdutosForm, EditProdutosForm

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
            form.save()
            redirect ('produtos:produtos')
    else:
        form = ProdutosForm()

    return render (request, 'pages/adicionar_produtos.htlm', context={
        'title': 'Adicionar produtos',
        'form': form
    })

def editar_produto(request, produtos_id):
    produto = get_object_or_404(Produtos, pk=produtos_id)
    if request.method == 'POST':
        form = EditProdutosForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            redirect('produtos:produtos')
    else:
        form = EditProdutosForm(instance=produto)

    return render (request, 'pages/adicionar_produtos.html', context={
        'title': 'Editar produto',
        'form': form
    })

def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produtos, pk=produto_id)
    
    produto.delete()
    return redirect ('produtos:produtos')