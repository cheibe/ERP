from django import forms
from app_fornecedores.models import Fornecedor

class FornecedorForm(forms.Form):

    class Meta:
        model = Fornecedor
        fields = [
            'nome',
            'telefone',
            'documentos',
            'rua',
            'numero',
            'bairro',
            'cidade',
            'estado'
        ]

class EditFornecedorForm(forms.Form):

    class Meta:
        model = Fornecedor
        fields = [
            'nome',
            'telefone',
            'documentos',
            'rua',
            'numero',
            'bairro',
            'cidade',
            'estado'
        ]