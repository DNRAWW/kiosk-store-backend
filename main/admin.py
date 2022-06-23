from urllib import request
from django.contrib import admin
from django import forms

from main.models import Category, Product, ProductImage

# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label="Имя")
    description = forms.Textarea()
    price = forms.DecimalField(min_value=1, label="Цена", decimal_places=2)
    category = forms.Select()

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance') is not None:
            kwargs['instance'].price = float(kwargs['instance'].price / 100)
        super(ProductForm, self).__init__(*args, **kwargs)


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    inlines = [ProductImageInline, ]

    def save_model(self, request, obj, form, change) -> None:
        price = form.cleaned_data.get('price')
        obj.price = int(price * 100)
        return super().save_model(request, obj, form, change)


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
