from django import forms
from app_produtos.models import Produtos

class ProdutosForm(forms.ModelForm):
    
    class Meta: 
        model = Produtos
        fields = [
            'codigo',
            'nome',
            'estoque',
            'preco_custo',
            'preco_venda',
            'embalagem',
        ]

class EditProdutosForm(forms.ModelForm):
    
    class Meta:
        model = Produtos
        fields = [
            'codigo',
            'nome',
            'estoque',
            'preco_custo',
            'preco_venda',
            'embalagem',
        ]