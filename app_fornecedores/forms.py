from django import forms
from app_fornecedores.models import Fornecedor

class FornecedorForm(forms.ModelForm):

    class Meta:
        model = Fornecedor
        fields = [
            'empresa',
            'nome',
            'telefone',
            'documento',
            'rua',
            'numero',
            'bairro',
            'cidade',
            'estado'
        ]
    
    def __init__(self, request, *args, **kwargs):
        super(FornecedorForm, self).__init__(*args, **kwargs)
        if not request.user.is_staff:
            del self.fields['empresa']

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