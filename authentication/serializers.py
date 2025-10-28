from .models import CustomUser
from djoser.serializers import UserCreateSerializer, UserSerializer

class CustomUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password']

class CustomUserSerializer(UserSerializer):
    class Meta (UserSerializer):
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name']
