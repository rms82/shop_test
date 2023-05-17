from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from product.models import Product, Color


class ProductSerializer(ModelSerializer):
    color = serializers.SlugRelatedField(slug_field='color', read_only=True, many=True)
    size = serializers.SlugRelatedField(slug_field='size', read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'


