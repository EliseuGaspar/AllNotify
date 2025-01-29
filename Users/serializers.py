from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth.models import User



class UserSerializerBase(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email", "password", "is_active"]

class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]

class UserEmptySerializer(Serializer):
    pass

