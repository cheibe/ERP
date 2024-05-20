import django_tables2 as tables
from app_produtos.models import Produtos

class ProdutosTable(tables.Table):
    codigo = tables.Column(verbose_name='Código', orderable=False)
    nome = tables.Column(verbose_name='Nome', orderable=False)
    preco_custo = tables.Column(verbose_name='Preço de custo', orderable=False)
    preco_venda = tables.Column(verbose_name='Preço de venda', orderable=False)
    estoque = tables.Column(verbose_name='Estoque', orderable=False)
    opcao = tables.TemplateColumn(template_name='pages/botao_acoes_produtos.html', verbose_name='Opções', orderable=False)

    class Meta:
        model = Produtos
        attrs = {'class': 'table table-bordered table-hover'}
        fields = ('codigo', 'nome', 'preco_custo', 'preco_venda', 'estoque')