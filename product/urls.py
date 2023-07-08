from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductCountHitDetailView.as_view(), name='product_detail'),
    path('like/<int:pk>/', views.LikeView.as_view(), name='like'),
    path('api/', include('product.api.urls')),
]
