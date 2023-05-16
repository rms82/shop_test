from django.urls import path

from . import views

urlpatterns = [
   path('', views.CartDetailView.as_view(), name='cart_detail'),
   path('add/<int:pk>/', views.AddToCartView.as_view(), name='cart_add'),
   path('add/order/', views.CreateOrderView.as_view(), name='add_order'),
   path('delete/<str:unique_id>/', views.DeleteCartItemView.as_view(), name='cart_delete'),

]
