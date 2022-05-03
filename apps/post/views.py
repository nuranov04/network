from rest_framework import viewsets

from apps.post.serializers import PostImageSerializer, PostSerializer, LikeSerializer
from apps.post.models import PostImage, Post, Like


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class PostImageViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
