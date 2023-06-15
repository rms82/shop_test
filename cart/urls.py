from django.urls import path

from . import views

urlpatterns = [
   # cart
   path('', views.CartDetailView.as_view(), name='cart_detail'),
   path('add/<int:pk>/', views.AddToCartView.as_view(), name='cart_add'),
   path('delete/<str:unique_id>/', views.DeleteCartItemView.as_view(), name='cart_delete'),

   # order
   path('add/order/', views.CreateOrderView.as_view(), name='add_order'),
   path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),

   # off code
   path('apply/code/<int:pk>/', views.OffCodeView.as_view(), name='off_code'),

]
