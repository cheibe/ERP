from rest_framework.response import Response
from rest_framework.decorators import api_view
from app_produtos.models import Produtos
from api.serializers import ProdutoSerializer

@api_view()
def produtos_api_list(request):
    produtos = Produtos.objects.all()[:20]
    serializer = ProdutoSerializer(instance=produtos, many=True)
    return Response(serializer.data)