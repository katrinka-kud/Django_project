from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import category, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', category, name='home'),
    path('categories/', product, name='categories')
]
