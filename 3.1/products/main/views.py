from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from rest_framework import status

from .serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer
from .models import Product, Review


@api_view(['GET'])
def products_list_view(request):
    """реализуйте получение всех товаров из БД
    реализуйте сериализацию полученных данных
    отдайте отсериализованные данные в Response"""

    products = Product.objects.all()
    ser = ProductListSerializer(products, many=True)
    return Response(ser.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        """реализуйте получение товара по id, если его нет, то выдайте 404
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""

        product = get_object_or_404(Product, pk=product_id)
        ser = ProductDetailsSerializer(product)
        return Response(ser.data)


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        product = get_object_or_404(Product, pk=product_id)
        mark = request.GET.get('mark')
        if mark:
            comments = product.comments.filter(mark=mark)
        else:
            comments = product.comments.all()

        ser = ReviewSerializer(comments, many=True)
        return Response(ser.data)


