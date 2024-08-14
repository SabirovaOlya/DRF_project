from django_filters import BooleanFilter
from rest_framework import filters
from .models import Category, Product


class ProductFilter(filters.SearchFilter):
    has_image = BooleanFilter(method='get_product_with_image')

    class Meta:
        model = Product
        fields = []

    def get_product_with_image(self, view, request):
        pass