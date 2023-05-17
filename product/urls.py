from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('api/', include('product.api.urls')),
]
