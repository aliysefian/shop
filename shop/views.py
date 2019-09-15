from django.shortcuts import render, get_object_or_404

# Create your views here.
from shop.models import Category, Product


def product_list(requset, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    return render(requset, 'shop/product/list.html', {'categories': categories, 'products': products})
