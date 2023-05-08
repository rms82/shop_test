from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

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
        color, size, quantity = request.POST.get('color'), request.POST.get('size'), request.POST.get('quantity')

        cart = Cart(request)
        cart.add_to_cart(product, color, size, quantity)

        return redirect('cart_detail')
