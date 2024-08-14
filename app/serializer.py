from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import CharField, BooleanField
from .models import Product, Category


class UserSerializer(serializers.ModelSerializer):
    password = CharField(write_only=True)
    is_active = BooleanField(read_only=True)

    class Meta:
        model = User
        fields = 'id', 'username'


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance: Category):
        repr = super().to_representation(instance)
        repr['products'] = ProductModelSerializer(instance.products)


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance: Product):
        repr = super().to_representation(instance)
        repr['category'] = CategoryModelSerializer(instance.category).data

        return repr
