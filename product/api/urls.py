from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductApiView

router = DefaultRouter()
router.register('viewset', ProductApiView, basename='product-api')

urlpatterns = [

]
urlpatterns += router.urls
