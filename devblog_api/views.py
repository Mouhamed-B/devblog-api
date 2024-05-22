from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoints that to manage posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTStatelessUserAuthentication]
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)