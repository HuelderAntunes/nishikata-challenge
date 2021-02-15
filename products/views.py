import json
from django.http import JsonResponse
from django.views.generic import TemplateView, View
from django.db.models import Sum
from django_pivot.pivot import pivot
from .models import ProductUrl


class ProductListView(TemplateView):
    template_name = 'products/list.html'


class ProductDataView(View):
    def get(self, request, *args, **kwargs):
        pivot_table = pivot(ProductUrl,
                            ['product_url', 'created_at'], 'consult_date',  'sales', default=0)

        queryset_with_sales = pivot_table.annotate(sales=Sum('sales'))

        return JsonResponse(list(queryset_with_sales), safe=False)
