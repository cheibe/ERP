import django_tables2 as tables
from app_empresas.models import Empresa

class EmpresaTable(tables.Table):
    nome_fantasia = tables.Column(verbose_name='Nome fantasia', orderable=False)
    cnpj = tables.Column(verbose_name='CNPJ', orderable=False)
    telefone_fixo = tables.Column(verbose_name='Telefone fixo', orderable=False)
    telefone_movel = tables.Column(verbose_name='Telefone movél', orderable=False)
    opcao = tables.TemplateColumn(template_name='pages/botao_acoes_empresa.html', verbose_name='Opções', orderable=False)

    class Meta:
        model = Empresa
        attrs = {'class': 'table table-bordered table-hover'}
        fields = ('nome_fantasia', 'cnpj', 'telefone_fixo', 'telefone_movel')