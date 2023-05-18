from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from product.models import Product, Color, Size, ProductFeature


class ProductSerializer(ModelSerializer):
    color = serializers.SlugRelatedField(slug_field='color', read_only=True, many=True)
    size = serializers.SlugRelatedField(slug_field='size', read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')

        if not request.parser_context.get('kwargs').get('pk'):
            rep.pop('description')
            rep.pop('image')
            rep.pop('off')

        return rep


class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class ProductFeatureSerializer(ModelSerializer):
    product = serializers.SlugRelatedField(many=False, slug_field='title', queryset=Product.objects.all())

    class Meta:
        model = ProductFeature
        fields = '__all__'
