from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import UserCreateSerializer

# Create your views here.

class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]