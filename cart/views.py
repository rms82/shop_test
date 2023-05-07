from django.shortcuts import render, redirect
from django.views.generic import View


# Create your views here.
class CartDetailView(View):
    def get(self, request):
        return render(request, 'cart/cart_detail.html', {})


class AddToCartView(View):
    def post(self, request):
        print(request.POST.get('color'))
        return redirect('cart_detail')
