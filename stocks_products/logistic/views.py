import django_filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

import django_filters.rest_framework
from rest_framework import generics


# class ProductList(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['title', 'id']

# class ProductListView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title',]

# class ProductFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(lookup_expr='iexact')
#
#     class Meta:
#         model = Product
#         fields = ['id',]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter]
    # filter_backends = [OrderingFilter]

    search_fields = ['products__id', 'products__title']
    # search_fields = ['products__title']
