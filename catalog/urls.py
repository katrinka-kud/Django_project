from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (ProductListView, CategoryListView, CategoryProductView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView, ProductDetailView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('categories/', ProductListView.as_view(), name='categories'),
    path('<int:pk>/products/', CategoryProductView.as_view(), name='category_products'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('detail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='detail_product'),
]
