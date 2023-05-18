from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from product.models import Product, Color, Size, ProductFeature
from .serializers import ProductSerializer, ColorSerializer, SizeSerializer, ProductFeatureSerializer


class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['size', 'color', ]
    search_fields = ['title', 'description', 'price']
    ordering_fields = ['price', ]

    @action(methods=['GET'], detail=False)
    def test(self, request):
        return Response({
            'response': 'Hi!!'
        })


class ColorApiView(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class SizeApiView(ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class ProductFeatureApiView(ModelViewSet):
    queryset = ProductFeature.objects.all()
    serializer_class = ProductFeatureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
