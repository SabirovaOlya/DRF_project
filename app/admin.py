from django.contrib import admin
from .models import Category, Product, ProductImage


class ProductImageStackedInline(admin.StackedInline):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
