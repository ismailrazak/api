from rest_framework import serializers
from    .models import Post
from django.contrib.auth import get_user_model
class Post_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id','author','title','body']


class USerSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields = ['username']