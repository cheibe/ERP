from django import forms
from app_pagamentos.models import Pagamento

class PagamentoForm(forms.ModelForm):

    class Meta:
        model = Pagamento
        fields = [
            'fornecedor',
            'descricao',
            'valor',
            'data_vencimento',
            'status',
        ]
        widgets = {
            'data_vencimento': forms.widgets.DateInput(attrs={'type': 'date'})
        }

class EditPagamentoForm(forms.ModelForm):

    class Meta:
        model = Pagamento
        fields = [
            'fornecedor',
            'descricao',
            'valor',
            'data_vencimento',
            'status',
        ]
        widgets = {
            'data_vencimento': forms.widgets.DateInput(attrs={'type': 'date'})
        }