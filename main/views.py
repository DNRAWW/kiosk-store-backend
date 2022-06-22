from unicodedata import category
from django.shortcuts import render
from rest_framework import viewsets
from main.models import Product, Category
from main.serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend, NumberFilter, FilterSet, ModelMultipleChoiceFilter
from rest_framework import filters

# Create your views here.


class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte')
    category = ModelMultipleChoiceFilter(
        field_name='category', queryset=Category.objects.all())


class ProductsViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['$name']


class CategoryViewset(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
