# Generated by Django 4.2.11 on 2024-04-05 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cep',
            field=models.CharField(max_length=8, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=models.CharField(max_length=14, null=True, verbose_name='CNPJ'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numero',
            field=models.CharField(max_length=5, verbose_name='Numero'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=11, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone_fixo',
            field=models.CharField(max_length=11, null=True, verbose_name='Telefone fixo'),
        ),
    ]
