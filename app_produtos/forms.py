from django import forms
from app_produtos.models import Produtos

class ProdutosForm(forms.ModelForm):
    
    class Meta: 
        model = Produtos
        fields = [
            'empresa',
            'codigo',
            'nome',
            'estoque',
            'preco_custo',
            'preco_venda',
            'embalagem',
        ]

    def __init__(self, request, *args, **kwargs):
        super(ProdutosForm, self).__init__(*args, **kwargs)
        if not request.user.is_staff:
            del self.fields['empresa']

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