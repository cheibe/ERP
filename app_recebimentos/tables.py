import django_tables2 as tables
from app_recebimentos.models import Recebimento

class RecebimentoTable(tables.Table):
    cliente = tables.Column(verbose_name='Cliente', orderable=False)
    data_emissao = tables.Column(verbose_name='Data emissão', orderable=False)
    data_vencimento = tables.Column(verbose_name='Data vencimento', orderable=False)
    status = tables.Column(verbose_name='Status', orderable=False)
    opcao = tables.TemplateColumn(template_name='pages/botao_acoes_recebimentos.html', verbose_name='Opções', orderable=False)
    class Meta:
        model = Recebimento
        attrs = {'class': 'table table-bordered table-hover'}
        fields = ('cliente', 'data_emissao', 'data_vencimento', 'status')