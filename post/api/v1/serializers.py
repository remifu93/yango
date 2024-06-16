from rest_framework import serializers
from post.models import Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title',)
