from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, Version


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Интернет-магазин женской обуви',
    }
    template_name = 'catalog/home.html'


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Стильно и удобно',
    }
    template_name = 'catalog/categories.html'


class CategoryProductView(TemplateView):
    template_name = 'catalog/products.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        category_pr = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['object_list'] = Product.objects.filter(category=self.kwargs.get('pk'))
        context_data['title'] = f'Все доступные к покупке {category_pr.name}'

        return context_data


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
