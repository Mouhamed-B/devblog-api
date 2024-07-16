from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth.models import User

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoints that to manage posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]
    authentication_classes = [JWTStatelessUserAuthentication]
    
    def perform_create(self, serializer):
        id = self.request.user.token['user_id']
        user = User.objects.get(id=id)
        serializer.save(author=user)
