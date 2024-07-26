from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.parsers import  MultiPartParser
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoints that to manage posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]
    authentication_classes = [JWTStatelessUserAuthentication]


    @action(
        detail=True,
        methods=["POST"],
        parser_classes=[MultiPartParser],
        url_path=r"upload/",
    )
    def upload(self, request, **kwargs):
        post = self.get_object()

        if "image" not in request.data:
            raise Response({
                'detail':'no image provided'
            }, status=status.HTTP_400_BAD_REQUEST)

        image = request.data["image"]
        post.image.save(image.name, image)
        return Response(PostSerializer(post).data)

    def perform_create(self, serializer):
        id = self.request.user.token['user_id']
        user = User.objects.get(id=id)
        serializer.save(author=user)
