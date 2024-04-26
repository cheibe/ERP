import django_tables2 as tables
from django.contrib.auth.models import User

class UsuarioTable(tables.Table):
    first_name = tables.Column(verbose_name='Primeiro nome', orderable=False)
    username = tables.Column(verbose_name='Usuário', orderable=False)
    email = tables.Column(verbose_name='E-mail', orderable=False)
    opcao = tables.TemplateColumn(template_name='pages/botao_acoes_usuarios.html', verbose_name='Opções', orderable=False)

    class Meta:
        model = User
        attrs = {'class': 'table table-bordered table-hover'}
        fields = ('first_name', 'username', 'email')