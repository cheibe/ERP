from rest_framework import serializers

class ProdutoSerializer(serializers.Serializer):
    codigo = serializers.CharField(max_length=5)
    nome = serializers.CharField(max_length=150)
    preco_custo = serializers.DecimalField(max_digits=15, decimal_places=2)
    preco_venda = serializers.DecimalField(max_digits=15, decimal_places=2)
    estoque = serializers.IntegerField()