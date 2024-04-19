from django.shortcuts import render
from app_pagamentos.models import Pagamento
from app_pagamentos.tables import PagamentoTable

def pagamentos_views(request):
    pagamentos = Pagamento.objects.all()
    table = PagamentoTable(pagamentos)
    return render(request, 'pages/pagamentos.html', context={
        'title': 'Pagamentos',
        'table': table
    })