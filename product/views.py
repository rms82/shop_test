from django.shortcuts import render
from django.views import generic
from hitcount.views import HitCountDetailView

from .models import Product, Color, Size


# Product Detail View with user_view count
class ProductCountHitDetailView(HitCountDetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'
    count_hit = True    # set to True if you want it to try and count the hit


# Product Detail View without user_view count
class ProductDetailView(generic.DetailView):
    template_name = 'product/product_detail.html'
    model = Product
    context_object_name = 'product'


class ProductListView(generic.ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'product/product_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        # For Showing color and size filter
        context['colors'] = Color.objects.all()
        context['sizes'] = Size.objects.all()

        return context
