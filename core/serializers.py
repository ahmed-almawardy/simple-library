from rest_framework.serializers import ModelSerializer
from core.models import Order, Book, Payment


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__' 


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

