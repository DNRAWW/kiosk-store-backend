import imp
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=50)

class Product(models.Model):
  name = models.CharField(max_length=50)
  price = models.BigIntegerField(validators=[MinValueValidator(1)])
  description = models.TextField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)