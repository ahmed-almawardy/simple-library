from re import I
from rest_framework.viewsets import ModelViewSet
from core.models import Book, Order, Payment
from core.serializers import OrderSerializer, BookSerializer, PaymentSerializer
from rest_framework.permissions import IsAdminUser


class OrderSimpleAPI(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser, )


class BookSimpleAPI(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class PaymentSimpleAPI(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (IsAdminUser, )
