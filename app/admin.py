from django.contrib import admin
from .models import Category, Product, ProductImage


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImage
    extra = 3
    min_num = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'name', 'price', )
    list_filter = ('name', 'price', 'category', )
    inlines = (ProductImageStackedInline,)
