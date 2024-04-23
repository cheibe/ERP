from django_tables2 import tables
from app_recebimentos.models import Recebimento

class RecebimentoTable(tables.Table):
    cliente = tables.columns(verbose_name='Cliente', orderable=False)
    data_emissao = tables.columns(verbose_name='Data emissão', orderable=False)
    data_vencimento = tables.columns(verbose_name='Data vencimento', orderable=False)
    status = tables.columns(verbose_name='Status', orderable=False)
    opcao = tables.TemplateColumn(tamplete_name='pages/botao_acoes.html', verbose_name='Opções', orderable=False)

    class Meta:
        model = Recebimento
        attrs = {'class': 'table table-bordered table-hover'}
        fields = ('cliente', 'data_emissao', 'data_vencimento', 'status')