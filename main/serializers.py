from dataclasses import field
from main.models import Category, Product, ProductImage

from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    image = serializers.URLField()

    class Meta:
        model = ProductImage
        fields = ['image']


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    category = CategorySerializer(many=False, read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'category', 'images']
        depth = 1
