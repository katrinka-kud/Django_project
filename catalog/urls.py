from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import product, CategoryListView, category_products, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('categories/', product, name='categories'),
    path('<int:pk>/products/', category_products, name='category_products'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]
