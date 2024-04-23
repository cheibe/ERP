from django import forms
from app_recebimentos.models import Recebimento

class RecebimentoForm(forms.ModelForm):

    class Meta:
        model = Recebimento
        fields = [
            'cliente',
            'descricao',
            'valor',
            'data_vencimento',
            'status',
        ]
        widgets = {
            'data_vencimento': forms.widgets.DateInput(attrs={'type': 'date'})
        }

class EditRecebimentoForm(forms.ModelForm):

    class Meta:
        model = Recebimento
        fields = [
            'cliente',
            'descricao',
            'valor',
            'data_vencimento',
            'status',
        ]
        widgets = {
            'data_vencimento': forms.widgets.DateInput(attrs={'type': 'date'})
        }