from django import forms
from app_clientes.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'razao_social',
            'nome_fantasia',
            'rg',
            'cnpj',
            'rua',
            'numero',
            'bairro',
            'cidade',
            'estado',
            'cep',
            'complemento',
            'telefone',
            'telefone_fixo',
        ]

class EditClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            'razao_social',
            'nome_fantasia',
            'rg',
            'cnpj',
            'rua',
            'numero',
            'bairro',
            'cidade',
            'estado',
            'cep',
            'complemento',
            'telefone',
            'telefone_fixo',
        ]