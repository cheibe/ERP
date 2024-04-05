from django.db import models

class Cliente(models.Model):
    razao_social = models.CharField(max_length=150, verbose_name='Razão social')
    nome_fantasia = models.CharField(max_length=150, null=True,verbose_name='Nome fantasia')
    rg = models.CharField(max_length=9, null=True, verbose_name='RG')
    cnpj = models.CharField(max_length=14, null=True, verbose_name='CNPJ')
    rua = models.CharField(max_length=50, verbose_name='Rua')
    numero = models.CharField(max_length=5, verbose_name='Numero')
    bairro = models.CharField(max_length=50, verbose_name='Bairro')
    cidade = models.CharField(max_length=50, verbose_name='Cidade')
    estado = models.CharField(max_length=2, verbose_name='Estado')
    cep = models.CharField(max_length=8, verbose_name='CEP')
    complemento = models.CharField(max_length=100, null=True, verbose_name='Complemento')
    telefone = models.CharField(max_length=11, verbose_name='Telefone')
    telefone_fixo = models.CharField(max_length=11, null=True, verbose_name='Telefone fixo')