from main.models import Category, Product

from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField()

class ProductSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField()
  price = serializers.IntegerField()
  description = serializers.CharField()
  category = serializers.PrimaryKeyRelatedField()
