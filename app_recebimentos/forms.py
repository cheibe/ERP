from django import forms
from app_recebimentos.models import Recebimento

class RecebimentoForm(forms.ModelForm):

    class Meta:
        model = Recebimento
        fields = [
            'empresa',
            'cliente',
            'descricao',
            'valor',
            'data_vencimento',
            'status',
        ]
        widgets = {
            'data_vencimento': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, request, *args, **kwargs):
        super(RecebimentoForm, self).__init__(*args, **kwargs)
        if not request.user.is_staff:
            del self.fields['empresa']

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