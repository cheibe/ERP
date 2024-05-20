import django_tables2 as tables
from app_clientes.models import Cliente

class ClienteTable(tables.Table):
    razao_social = tables.Column(verbose_name='Razão social', orderable=False)
    nome_fantasia = tables.Column(verbose_name='Nome fantasia', orderable=False)
    telefone = tables.Column(verbose_name='Telefone', orderable=False)
    telefone_fixo = tables.Column(verbose_name='Telefone fixo', orderable=False)
    opcao = tables.TemplateColumn(template_name='pages/botao_opcoes_clientes.html', verbose_name='Opções', orderable=False)

    class Meta:
        model = Cliente
        attrs = {'class': 'table table-bordered table-hover'}
        fields = ('razao_social', 'nome_fantasia', 'telefone', 'telefone_fixo')