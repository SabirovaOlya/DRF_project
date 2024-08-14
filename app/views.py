from rest_framework.generics import ListCreateAPIView
from .models import Product, Category
from .serializer import ProductModelSerializer, CategoryModelSerializer


class ProductListApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class CategoryListApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    filter_class
