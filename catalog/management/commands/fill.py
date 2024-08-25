import json
from pathlib import Path

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        ROOT_PATH = Path(__file__).parent.parent.parent.parent
        DATA_PATH = ROOT_PATH.joinpath('catalog.json')
        with open(DATA_PATH, 'rt', encoding="UTF-8") as file:
            catalog = json.load(file)

        category_for_create = []
        product_for_create = []

        for category in catalog:
            data = category['fields']
            if category['model'] == 'catalog.category':
                category_for_create.append(Category(
                    category_name=data['category_name'],
                    category_description=data.get('category_description', None),
                    pk=category['pk']
                ))
        Category.objects.bulk_create(category_for_create)

        for product in catalog:
            data = product['fields']
            if product['model'] == 'catalog.product':
                valid_cat = Category.objects.get(pk=data.get('category')) if data['category'] else None
                product_for_create.append(Product(
                    pk=product['pk'],
                    product_name=data['product_name'],
                    product_description=data['product_description'],
                    product_image=data['product_image'],
                    category=valid_cat,
                    price=data['price'],
                    created_at=data['created_at'],
                    created_up=data['created_up'],
                ))
        Product.objects.bulk_create(product_for_create)


