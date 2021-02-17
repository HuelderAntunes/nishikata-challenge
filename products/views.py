from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.views.generic import TemplateView, View
from django.db.models import Sum
from django_pivot.pivot import pivot
from .models import ProductUrl
from .utils import get_queryset_column_model_names


class ProductListView(TemplateView):
    template_name = 'products/list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)

        queryset = pivot(ProductUrl,
                         ['product_url', 'created_at'],
                         'consult_date',
                         'sales', default=0).annotate(sales=Sum('sales')).first()

        columns = get_queryset_column_model_names(ProductUrl, queryset)

        context['columns'] = columns

        return context


class ProductDataView(ListAPIView):
    queryset = ProductUrl

    def filter_queryset(self, queryset):
        queryset = super(ProductDataView, self).filter_queryset(queryset)

        queryset = pivot(ProductUrl,
                         ['product_url', 'created_at'],
                         'consult_date',
                         'sales',
                         default=0
                         ).annotate(sales=Sum('sales')).order_by('product_url')
        return queryset

    def get_serializer_class(self):
        return None

    # Overrides ListModelMixin "list()" method to excludes need of a serializer
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)

        if page is not None:
            return self.get_paginated_response(page)

        return Response(queryset)
