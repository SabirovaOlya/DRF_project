from rest_framework.generics import ListCreateAPIView
from .models import Product, Category
from .serializer import ProductModelSerializer, CategoryModelSerializer
from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 10


class ProductListApiView(ListCreateAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductModelSerializer


class CategoryListApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
