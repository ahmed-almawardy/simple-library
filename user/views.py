from user.models import Author, User
from user.permisions import IsOwner
from user.serializers import UserSerializer, AuthorSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser


class UserSimpleAPI(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, IsOwner)


class AuthorSimpleAPI(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
