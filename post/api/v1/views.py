from rest_framework.generics import ListAPIView

from post.models import Post
from .serializers import PostListSerializer


class PostListAPiView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
