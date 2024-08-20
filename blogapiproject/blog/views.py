from rest_framework import generics , permissions
from .models import Post
from .serializers import Post_Serializer,USerSerializer
from .permissions import isUserOrReadyOnly
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class PostViewSet(ModelViewSet):
    permission_classes = isUserOrReadyOnly,
    queryset = Post.objects.all()
    serializer_class = Post_Serializer

class UserViewSet(ModelViewSet):
    permission_classes = permissions.IsAdminUser,
    queryset = get_user_model().objects.all()
    serializer_class = USerSerializer
