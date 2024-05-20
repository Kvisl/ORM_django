from rest_framework import serializers
from main.models import Book, Order


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['author', 'title', 'year']
    # реализуйте сериализацию объектов модели Book


    #доп задание
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        orders_count = instance.order_set.count()
        representation['orders_count'] = orders_count
        return representation


class OrderSerializer(serializers.ModelSerializer):
    # добавьте поля модели Order
    class Meta:
        model = Order
        fields = ['user_name', 'days_count', 'date', 'books']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['books'] = BookSerializer(instance.books.all(), many=True).data
        return representation
