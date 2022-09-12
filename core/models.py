from locale import currency
from statistics import mode
from django.db import models

class Book(models.Model):
    title = models.CharField('Title', max_length=250)
    pg_no = models.PositiveSmallIntegerField('Page no')
    description =  models.TextField('Description')
    isbn = models.CharField('ISBN', max_length=35)
    price = models.DecimalField('Book price', max_digits=5, decimal_places=2)
    link = models.CharField('Book link', max_length=250)
    currency = models.PositiveSmallIntegerField('Currency', choices=(
        (1, 'ruble'),
        (2, 'usd'),
    ))

    def __str__(self) -> str:
        return  str(self.title)


class Payment(models.Model):
    buyer = models.ForeignKey('user.User', related_name='payments', on_delete=models.DO_NOTHING)
    order = models.ForeignKey('core.Order', related_name='payments', on_delete=models.DO_NOTHING)
    payment_mehod = models.CharField(choices=(
        ('card','CARD'),
        ('cash','CASH'),
    ), max_length=35)
    created_at = models.DateTimeField('paid at', auto_now=True)
    status = models.CharField(choices=(
        ('ok', 'OK'),
        ('error', 'ERROR'),
    ),max_length=30)
    dscription = models.TextField(null=True, blank=True)
    amount = models.DecimalField('Amount', decimal_places=2, max_digits=5)
    currency = models.CharField('Currency', choices=(
        ('ru-ruble', 'ru-RUB'),
        ('usd', 'USD'),
    ), max_length=35)
    
    def __str__(self) -> str:
        return f'Payment for: {self.order}'


class Order(models.Model):
    title = models.CharField('Title', max_length=250)
    buyer = models.ForeignKey('user.User', related_name='orders', on_delete=models.DO_NOTHING)
    books = models.ManyToManyField('core.Book', related_name='orders')
    status = models.CharField(choices=(
        ('started', 'START'),
        ('in_work', 'WORK'),
        ('paid', 'PAID'),
        ('unpaid', 'NO-PAID'),
        ('deliverd', 'SHHIPED'),
        ('refund', 'REFUND'),
    ),max_length=45)
    created_at = models.DateTimeField('created at', auto_now=True)

    def __str__(self) -> str:
        return str(self.title)
    
    @property
    def price(self):
        total_price = 0
        for book in self.books.all():
            total_price+=book.price
        return f'{total_price} {book.currency}' 