from django.shortcuts import render
from django.views import generic

from .models import Product


# Create your views here.
class ProductDetailView(generic.DetailView):
    template_name = 'product/product_detail.html'
    model = Product
    context_object_name = 'product'
