from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}