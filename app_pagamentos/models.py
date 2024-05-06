from django.db import models
from app_fornecedores.models import Fornecedor
from app_empresas.models import Empresa

PAGAMENTO_STATUS = [
    ('pendente', 'Pendente'),
    ('pago', 'Pago'),
    ('cancelado', 'Cancelado'),
]

class Pagamento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255, verbose_name='Descrição')
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    data_emissao = models.DateField(auto_now_add=True, verbose_name='Data de Emissão')
    data_vencimento = models.DateField(verbose_name='Data de Vencimento')
    status = models.CharField(max_length=30, choices=PAGAMENTO_STATUS, default='pendente')

    def __str__(self):
        return self.fornecedor.nome