from django import forms
from app_clientes.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'empresa',
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

    def __init__(self, request, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        if not request.user.is_staff:
            del self.fields['empresa']

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