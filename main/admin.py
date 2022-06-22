from django.contrib import admin
from django import forms

from main.models import Category, Product, ProductImage

# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ProductForm(forms.ModelForm):
    price = forms.DecimalField(min_value=1)

    class Meta:
        model = Product
        exclude = ['price']


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]

    def save_model(self, request, obj, form, change):
        obj.price = obj.price * 100
        super().save_model(request, obj, form, change)


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
