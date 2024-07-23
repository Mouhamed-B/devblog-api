from posts_api.models import Post
from posts_api.serializers import PostSerializer
from rest_framework.generics import ListAPIView

# Create your views here.

class AuthorPostListView(ListAPIView):
    """
    API endpoint that list author post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer