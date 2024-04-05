from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Category


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    extra_context = {
        'title': 'Интернет-магазин женской обуви',
    }
    template_name = 'catalog/home.html'


# def category(request):
#     content = {
#         'products': Category.objects.all(),
#         'title': 'Интернет-магазин женской обуви',
#     }
#     return render(request, 'catalog/home.html', content)


def product(request):
    content = {
        'products': Product.objects.all(),
        'title': 'Стильно и удобно',
        'description': f'Возможные варианты {Product.objects.all()}',
    }
    return render(request, 'catalog/categories.html', content)


# class CategoryProductView(TemplateView):
#     template_name = 'catalog/products.html'
#
#     def category_products(self, **kwargs):
#         context_data = super().category_products(**kwargs)
#         category_pr = Category.objects.get(pk=self.kwargs.get('pk'))
#         context_data['products'] = Product.objects.filter(category=self.kwargs.get('pk'))
#         context_data['title'] = f'Все доступные к покупке {category_pr.name}'
#
#         return context_data


def category_products(request, pk):
    category_item = Category.objects.get(pk=pk)
    content = {
        'products': Product.objects.filter(category_id=pk),
        'title': f'Все доступные к покупке {category_item.name}',
    }
    return render(request, 'catalog/products.html', content)


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'price', 'description', 'category', 'image')
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'price', 'description', 'category', 'image')
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
