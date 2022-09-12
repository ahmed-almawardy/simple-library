from django.urls import path,include
from rest_framework.routers import DefaultRouter
from user import views


app_name = 'users'
api_user_router = DefaultRouter()
api_user_router.register('', views.UserSimpleAPI, basename='users-api')

api_author_router = DefaultRouter()
api_author_router.register('', views.AuthorSimpleAPI, basename='author-api')

urlpatterns = [
    path("users/", include(api_user_router.urls)),
    path("authors/", include(api_author_router.urls)),
]
