from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from core.models import Book, Order
from user.models import Author, User


class UserSerializer(ModelSerializer):
    books = PrimaryKeyRelatedField(queryset = Book.objects.all(), many=True)
    orders = PrimaryKeyRelatedField(queryset = Order.objects.all(), many=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'password', 'last_name', 'is_staff', 'is_superuser', 'books', 'orders',]
        extra_kwargs = {
            'password': {'write_only': True, 'style':{'input_type': 'password', 'placeholder': 'Password'}},
            'is_superuser': {'read_only': True, },
        }

    def create(self, validated_data):
        if validated_data.get('is_staff'):
           return self.Meta.model.objects.create_superuser(**validated_data, is_superuser=True) 
        return self.Meta.model.objects.create_user(**validated_data)
    


class AuthorSerializer(ModelSerializer):
    books = PrimaryKeyRelatedField(queryset = Book.objects.all(), many=True)
    class Meta:
        model = Author
        fields = '__all__'
        