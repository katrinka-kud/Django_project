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
