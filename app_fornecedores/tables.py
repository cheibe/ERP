import django_tables2 as tables
from app_fornecedores.models import Fornecedor

class FornecedorTable(tables.Table):
    nome = tables.Column(verbose_name='Nome', orderable=False)
    telefone = tables.Column(verbose_name='Telefone', orderable=False)
    cidade = tables.Column(verbose_name='Cidade', orderable=False)
    opcao = tables.TemplateColumn(template_name='pages/botao_acoes_fornecedores.html', verbose_name='Opções', orderable=False)

    class Meta:
        model = Fornecedor
        attrs = {'class': 'table table-bordered table-hover'}
        fields = ('nome', 'telefone', 'cidade')