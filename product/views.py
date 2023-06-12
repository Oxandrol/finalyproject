from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.serializers import ProductListSerializer
from product.serializers import CategoryListSerializer
from product.serializers import ReviewListSerializer
from product.models import Product
from product.models import Category
from product.models import Review


@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    data = ProductListSerializer(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error_message': 'Product not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ProductListSerializer(product).data
    return Response(data=data)


@api_view(['GET'])
def category_list_api_view(request):
    category = Category.objects.all()
    data = ProductListSerializer(category, many=True).data
    return Response(data=data)


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error_message': 'Product not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = CategoryListSerializer(category).data
    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):
    review = Review.objects.all()
    data = ProductListSerializer(review, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error_message': 'Product not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewListSerializer(review).data
    return Response(data=data)
