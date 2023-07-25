from django.shortcuts import render
from django.views import View
from .models import Category, Product
from django.shortcuts import get_object_or_404
# Create your views here.


class StoreView(View):

    def get(self, request):
        all_products = Product.objects.all()

        return render(request, 'store/store.html', context={
            "all_products": all_products
        })


def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}


class SingleProductView(View):

    def get(self, request, slug):

        product = get_object_or_404(Product, slug=slug)

        return render(request, 'store/product-info.html', context={
            'product': product
        })


class CategoriesView(View):

    def get(self, request, slug):

        category = get_object_or_404(Category, slug=slug)

        products = Product.objects.filter(category=category)

        return render(request, 'store/list-category.html', context={
            'products': products,
            'category': category,
        })
