from django.db import models

EMBALAGEM_DE_VENDA = [
    ('caixa', 'Caixa'),
    ('duzia', 'Duzia'),
    ('unidade', 'Unidade'),
    ('kilo', 'Kilo'),
    ('peca', 'Peça'),
    ('embalagem', 'Embalagem'),
    ('metro', 'Metro'),
    ('outros', 'Outros'),
]

class Produtos(models.Model):
    codigo = models.CharField(max_length=5, verbose_name='Código')
    nome = models.CharField(max_length=150, verbose_name='Nome')
    estoque = models.IntegerField(verbose_name='Estoque')
    preco_custo = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Preço de custo')
    preco_venda = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Preço de venda')
    embalagem = models.CharField(max_length=35, choices=EMBALAGEM_DE_VENDA, verbose_name='Embalagem')

    def __str__(self):
        return self.nome