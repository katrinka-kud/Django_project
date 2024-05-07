from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_cached_products_list():
    """Получает данные из кэша, если кэш пуст, получает данные из БД"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'products_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products
