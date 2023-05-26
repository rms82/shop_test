from django.urls import reverse
from django.test import TestCase

from .models import Size, Color, Product, ProductFeature


class SizeModelTestCase(TestCase):
    def setUp(self):
        self.size = Size.objects.create(size='Small')

    def test_size_creation(self):
        size = Size.objects.get(size='Small')
        self.assertEqual(size.size, 'Small')


class ColorModelTestCase(TestCase):
    def setUp(self):
        self.color = Color.objects.create(color='Red')

    def test_color_creation(self):
        color = Color.objects.get(color='Red')
        self.assertEqual(color.color, 'Red')


class ProductModelTestCase(TestCase):
    def setUp(self):
        self.size = Size.objects.create(size='Small')
        self.color = Color.objects.create(color='Red')
        self.product = Product.objects.create(
            title='Test Product',
            description='Test Description',
            price=10,
            image='test_image.jpg'
        )
        self.product.size.add(self.size)
        self.product.color.add(self.color)

    def test_product_creation(self):
        product = Product.objects.get(title='Test Product')
        self.assertEqual(product.description, 'Test Description')
        self.assertEqual(product.price, 10)
        self.assertEqual(product.image, 'test_image.jpg')
        self.assertEqual(product.size.first().size, 'Small')
        self.assertEqual(product.color.first().color, 'Red')


class ProductFeatureModelTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            title='Test Product',
            description='Test Description',
            price=10,
            image='test_image.jpg'
        )
        self.product_feature = ProductFeature.objects.create(
            title='Test Feature',
            product=self.product
        )

    def test_product_feature_creation(self):
        product_feature = ProductFeature.objects.get(title='Test Feature')
        self.assertEqual(product_feature.product, self.product)


class ProductDetailViewTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            title='Test Product',
            description='Test Description',
            price=10,
            image='test_image.jpg'
        )
        self.url = reverse('product_detail', kwargs={'pk': self.product.pk})

    def test_product_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_detail.html')
        self.assertEqual(response.context['product'], self.product)
        self.assertContains(response, 'Test Product')
        self.assertContains(response, 'Test Description')
        self.assertContains(response, '10')
        self.assertContains(response, 'test_image.jpg')
