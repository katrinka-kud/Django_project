from django.shortcuts import render

from catalog.models import Product, Category


def category(request):
    content = {
        'products': Category.objects.all(),
        'title': 'Интернет-магазин женской обуви',
    }
    return render(request, 'catalog/home.html', content)


def product(request):
    content = {
        'products': Product.objects.all(),
        'title': 'Стильно и удобно',
        'description': f'Возможные варианты {Product.objects.all()}',
    }
    return render(request, 'catalog/categories.html', content)


def category_products(request, pk):
    category_item = Category.objects.get(pk=pk)
    content = {
        'products': Product.objects.filter(category_id=pk),
        'title': f'Все доступные к покупке {category_item.name}',
    }
    return render(request, 'catalog/products.html', content)
