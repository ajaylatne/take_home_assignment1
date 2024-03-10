from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )
        return user


# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=20)
#     password = serializers.CharField(max_length=20)

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author']
