from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import category, product, category_products

app_name = CatalogConfig.name

urlpatterns = [
    path('', category, name='home'),
    path('categories/', product, name='categories'),
    path('<int:pk>/products/', category_products, name='category_products'),
]
