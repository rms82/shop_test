from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class CartDetailView(TemplateView):
    template_name = 'cart/cart_detail.html'
