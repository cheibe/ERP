from django import forms
from app_fornecedores.models import Fornecedor

class FornecedorForm(forms.ModelForm):

    class Meta:
        model = Fornecedor
        fields = [
            'nome',
            'telefone',
            'documento',
            'rua',
            'numero',
            'bairro',
            'cidade',
            'estado'
        ]

class EditFornecedorForm(forms.ModelForm):

    class Meta:
        model = Fornecedor
        fields = [
            'nome',
            'telefone',
            'documento',
            'rua',
            'numero',
            'bairro',
            'cidade',
            'estado'
        ]