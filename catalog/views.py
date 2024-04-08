from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.models import Product, Category


class CategoryListView(ListView):
    """Выводит все категории на главной странице"""
    model = Category
    extra_context = {
        'title': 'Интернет-магазин женской обуви',
    }
    template_name = 'catalog/home.html'


class ProductListView(ListView):
    """Показывает все доступные модели"""
    model = Product
    extra_context = {
        'title': 'Стильно и удобно',
    }
    template_name = 'catalog/categories.html'


class CategoryProductView(TemplateView):
    """Показывает модели, соответствующей категории"""
    template_name = 'catalog/products.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        category_pr = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['object_list'] = Product.objects.filter(category=self.kwargs.get('pk'))
        context_data['title'] = f'Все доступные к покупке {category_pr.name}'

        return context_data


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
