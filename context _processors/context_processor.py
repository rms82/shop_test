from product.models import Category


def category(request):
    categories = Category.objects.all()

    return {
        'category': categories
    }
