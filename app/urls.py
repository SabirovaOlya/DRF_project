from django.urls import path
from .views import ProductListApiView, CategoryListApiView

urlpatterns = [
    path('products', ProductListApiView.as_view()),
    #path('products/<uuid:pk>', ProductListApiView.as_view()),
    path('categories', CategoryListApiView.as_view()),
    #path('categories/<uuid:pk>', CategoryListApiView.as_view()),
]
