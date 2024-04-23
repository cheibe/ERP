# Generated by Django 4.2.11 on 2024-04-18 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_fornecedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrção')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('data_emissao', models.DateField(auto_now_add=True, verbose_name='Data de Emissão')),
                ('data_vencimento', models.DateField(verbose_name='Data de Vencimento')),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('pago', 'Pago'), ('cancelado', 'Cancelado')], default='pendente', max_length=30)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_fornecedores.fornecedor')),
            ],
        ),
    ]