from rest_framework import serializers
from product.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'category'.split()


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'product'.split()

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product