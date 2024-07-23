from django.urls import path
from .views import AuthorPostListView

urlpatterns = [
    path('posts', AuthorPostListView.as_view(), name='author_post_list')
]