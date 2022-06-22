from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    price = models.BigIntegerField(
        validators=[MinValueValidator(1)], verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="images/", verbose_name="Картинка")

    class Meta:
        verbose_name = "Картинку"
        verbose_name_plural = "Картинки"
