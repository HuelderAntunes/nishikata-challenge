from rest_framework.response import Response
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from django.core.management import call_command
from .models import ProductUrl


class TestProductUrl(TestCase):
    def setUp(self):
        call_command('populate')

    def test_model_str(self):
        self.assertEquals(str(ProductUrl.objects.get(
            pk=1)), 'https://baebrow.com/products/baebrow-instant-tint-graphite')

    def test_get_model_column(self):
        self.assertEquals(ProductUrl.get_column_name(
            'created_at'), 'Data inserção na loja')
        self.assertEquals(ProductUrl.get_column_name(
            'sales'), 'Total de vendas')
        self.assertEquals(ProductUrl.get_column_name(
            'product_url'), 'Produto')


class TestProductListView(TestCase):
    def test_response(self):
        response = self.client.get(reverse('products:list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/list.html')

    def test_page_content(self):
        response = self.client.get(reverse('products:list'))
        self.assertContains(
            response, '<script src="https://cdn.datatables.net/1.10.23/js/jquery.dataTables.min.js"></script>')
        self.assertContains(
            response, '<table id="product_list" class="display" style="width: 100%">')


class TestProductDataView(APITestCase):
    def setUp(self):
        call_command('populate')

    def test_response(self):
        response = self.client.get(reverse('products:data'), format='json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(type(response), Response)

    def test_data_integrity(self):
        response = self.client.get(reverse('products:data'), format='json')

        self.assertEquals(response.json()['count'], 417)
        self.assertEquals(22, response.json()['results'][0]['sales'])
