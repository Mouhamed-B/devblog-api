from posts_api.models import Post
from posts_api.serializers import PostSerializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.

class AuthorPostListView(ListAPIView):
    """
    API endpoint that list author post.
    """

    serializer_class = PostSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        user_id = self.request.user.token['user_id']
        author = User.objects.get(id=user_id)

        queryset = Post.objects.filter(author=author)
        serializer_class = self.get_serializer_class()
        
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)