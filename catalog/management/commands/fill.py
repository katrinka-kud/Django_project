from django.core.management import BaseCommand

from catalog.models import Product, Category
import json

from config.settings import BASE_DIR

FIXTURES_BASE_DIR = BASE_DIR.joinpath('fixtures')


class Command(BaseCommand):

    @staticmethod
    def _read_fixtures(fixture_file_name: str):
        fixture_path = FIXTURES_BASE_DIR.joinpath(fixture_file_name)
        with fixture_path.open(encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def json_read_categories():
        return Command._read_fixtures('categories.json')

    @staticmethod
    def json_read_products():
        return Command._read_fixtures('products.json')

    def handle(self, *args, **options):
        product_for_create = []
        category_for_create = []
        Category.objects.all().delete()
        Product.objects.all().delete()
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(pk=category['pk'],
                         name=category['fields']['name'],
                         description=category['fields']['description'])
            )

        Category.objects.bulk_create(category_for_create)
        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product['fields']['name'],
                        description=product['fields']['description'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price'])
            )
        Product.objects.bulk_create(product_for_create)
