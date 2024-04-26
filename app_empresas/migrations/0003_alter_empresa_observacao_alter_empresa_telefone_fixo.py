# Generated by Django 4.2.11 on 2024-04-25 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_empresas', '0002_alter_empresa_telefone_fixo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='observacao',
            field=models.CharField(blank=True, max_length=255, verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefone_fixo',
            field=models.CharField(blank=True, max_length=10, verbose_name='Telefone fixo'),
        ),
    ]