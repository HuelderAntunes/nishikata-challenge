from django.core.management.base import BaseCommand, CommandError
from products.models import ProductUrl
from products.data import data


class Command(BaseCommand):
    help = 'Insert fake data in database.'

    def handle(self, *args, **options):
        ProductUrl.objects.all().delete()
        products_url = [ProductUrl(product_url=product['product_url'],
                                   consult_date=product['consult_date'],
                                   created_at=product['product_url__created_at'],
                                   image=product['product_url__image'],
                                   store_url=product['store_url'],
                                   sales=product['c']) for product in data]

        ProductUrl.objects.bulk_create(products_url)

        print("The data was entered successfully.")
