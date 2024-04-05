from django import forms
from app_clientes.models import Cliente

class ClienteForm(forms.ModelForm):
    
    model = Cliente
    fields = [
        'razao_social',
        'nome_fantasa',
        'rg',
        'cnpj',
        'rua',
        'numero',
        'bairro',
        'cidade',
        'estado',
        'cep',
        'complemeto',
        'telefone',
        'telefone_fixo',
    ]

class EditClienteForm(forms.ModelForm):

    model = Cliente
    fields = [
        'razao_social',
        'nome_fantasa',
        'rg',
        'cnpj',
        'rua',
        'numero',
        'bairro',
        'cidade',
        'estado',
        'cep',
        'complemeto',
        'telefone',
        'telefone_fixo',
    ]