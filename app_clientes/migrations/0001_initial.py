# Generated by Django 4.2.11 on 2024-04-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=150, verbose_name='Razão social')),
                ('nome_fantasia', models.CharField(max_length=150, null=True, verbose_name='Nome fantasia')),
                ('rg', models.CharField(max_length=9, null=True, verbose_name='RG')),
                ('cnpj', models.IntegerField(max_length=14, null=True, verbose_name='CNPJ')),
                ('rua', models.CharField(max_length=50, verbose_name='Rua')),
                ('numero', models.IntegerField(max_length=5, verbose_name='Numero')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('cep', models.IntegerField(max_length=8, verbose_name='CEP')),
                ('complemento', models.CharField(max_length=100, null=True, verbose_name='Complemento')),
                ('telefone', models.IntegerField(max_length=11, verbose_name='Telefone')),
                ('telefone_fixo', models.IntegerField(max_length=11, null=True, verbose_name='Telefone fixo')),
            ],
        ),
    ]
