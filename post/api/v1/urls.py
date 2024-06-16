from django.urls import path
from .views import PostListAPiView


urlpatterns = [
    path("", PostListAPiView.as_view(), name="post-api-list"),
]
