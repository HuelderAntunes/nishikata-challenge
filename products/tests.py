from django.http.response import JsonResponse
from django.urls import reverse
from django.test import TestCase
from django.core.management import call_command
from .models import ProductUrl


class TestProductUrl(TestCase):
    def setUp(self):
        call_command('populate')

    def test_model_str(self):
        self.assertEquals(str(ProductUrl.objects.get(
            pk=1)), 'https://baebrow.com/products/baebrow-instant-tint-graphite')


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


class TestProductDataView(TestCase):
    def setUp(self):
        call_command('populate')

    def test_response(self):
        response = self.client.get(reverse('products:data'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(type(response), JsonResponse)

    def test_data_integrity(self):
        response = self.client.get(reverse('products:data'))

        self.assertEquals(len(response.json()), 417)

        self.assertDictEqual(response.json()[0], {
            "product_url": "https://baebrow.com/products/baebrow-instant-tint-graphite",
            "created_at": "2019-06-26T18:28:02Z",
            "2021-02-09": 0,
            "2021-02-10": 0,
            "2021-02-11": 6,
            "2021-02-12": 10,
            "2021-02-13": 6,
            "2021-02-14": 0,
            "sales": 22
        })
