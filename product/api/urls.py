from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductApiView, ColorApiView, SizeApiView, ProductFeatureApiView

router = DefaultRouter()
router.register('product', ProductApiView, basename='product-api')
router.register('color', ColorApiView, basename='color-api')
router.register('size', SizeApiView, basename='size-api')
router.register('product_feature', ProductFeatureApiView, basename='product_feature')

urlpatterns = [

]
urlpatterns += router.urls
