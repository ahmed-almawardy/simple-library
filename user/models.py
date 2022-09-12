from wsgiref.simple_server import demo_app
from django.db import models
from django.contrib.auth.models import AbstractUser

class Author(models.Model):
    name = models.CharField('Author', max_length=200)
    books = models.ManyToManyField('core.Book', related_name='authors')
    email = models.EmailField(('email address'), max_length=250, null=True, blank=True) # authors don't use auth sytem

class User(AbstractUser):
    books = models.ManyToManyField('core.Book', related_name='readers')
    email = models.EmailField(('email address'), unique=True, max_length=250)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']