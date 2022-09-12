from django.urls import path,include
from rest_framework.routers import DefaultRouter
from core import views


app_name = 'core'
api_order_router = DefaultRouter()
api_order_router.register('', views.OrderSimpleAPI, basename='order-api')

api_payment_router = DefaultRouter()
api_payment_router.register('', views.PaymentSimpleAPI, basename='payment-api')

api_book_router = DefaultRouter()
api_book_router.register('', views.BookSimpleAPI, basename='book-api')

urlpatterns = [
    path("books/", include(api_book_router.urls)),
    path("orders/", include(api_order_router.urls)),
    path("payments/", include(api_payment_router.urls)),
]
