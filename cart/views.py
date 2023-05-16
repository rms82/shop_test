from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView

from cart.cart import Cart
from product.models import Product


# Create your views here.
class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)

        return render(request, 'cart/cart_detail.html', {'cart': cart})


class AddToCartView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        color, size, quantity = request.POST.get('color', 'default'), request.POST.get('size',
                                                                                       'default'), request.POST.get(
            'quantity', 1)

        if quantity == '0':
            quantity = 1

        cart = Cart(request)
        cart.add_to_cart(product, color, size, quantity)

        return redirect('cart_detail')


class DeleteCartItemView(View):
    def get(self, request, unique_id):
        cart = Cart(request)
        cart.delete_item(unique_id)

        return redirect('cart_detail')


