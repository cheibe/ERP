from django import forms
from app_empresas.models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'razao_social',
            'nome_fantasia',
            'cnpj',
            'ie', 
            'telefone_fixo',
            'telefone_movel',
            'observacao',
        ]

class EditEmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'razao_social',
            'nome_fantasia',
            'cnpj',
            'ie', 
            'telefone_fixo',
            'telefone_movel',
            'observacao',
        ]