from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from hitcount.views import HitCountDetailView

from .models import Product, Color, Size, Like


# Product Detail View with user_view count
class ProductCountHitDetailView(HitCountDetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'
    count_hit = True  # set to True if you want it to try and count the hit


# Product Detail View without user_view count
class ProductDetailView(generic.DetailView):
    template_name = 'product/product_detail.html'
    model = Product
    context_object_name = 'product'


class ProductListView(generic.ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'product/product_list.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        # For Showing color and size filter
        context['colors'] = Color.objects.all()
        context['sizes'] = Size.objects.all()

        return context


class LikeView(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        try:
            like = Like.objects.get(product_id=pk, user=self.request.user)
            like.delete()
            response = {'like': False}

        except Like.DoesNotExist:
            Like.objects.create(user=self.request.user, product_id=pk)
            response = {'like': True}

        return JsonResponse(response)
