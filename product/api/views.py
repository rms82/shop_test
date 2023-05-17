from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from product.models import Product
from .serializers import ProductSerializer


class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(methods=['GET'], detail=False)
    def test(self, request):
        return Response({
            'response': 'Hi!!'
        })

