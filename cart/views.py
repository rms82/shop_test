from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from cart.cart import Cart
from cart.models import Order, OrderItem, OffCode
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


class CreateOrderView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        if len(cart) == 0:
            return redirect('home')

        order = Order.objects.create(user=request.user, total_price=cart.total_cart())
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'],
                                     color=item['color'], size=item['size'], total=item['total'])
        cart.clear()

        return redirect('order_detail', order.id)


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)

        return render(request, 'cart/order_detail.html', {'order': order})


class OffCodeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        code = request.POST.get('off_code')

        if code:
            off_code = get_object_or_404(OffCode, code=code)

            if off_code.quantity >= 1:
                order.total_price -= (off_code.off / 100) * order.total_price
                order.save()

                off_code.quantity -= 1
                off_code.save()

        return redirect('order_detail', pk)
