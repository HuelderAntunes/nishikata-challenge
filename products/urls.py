from django.urls import path
from .views import ProductListView, ProductDataView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('data/', ProductDataView.as_view(), name='data')
]
