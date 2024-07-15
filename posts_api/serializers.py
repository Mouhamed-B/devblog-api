from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author','slug','date_posted']