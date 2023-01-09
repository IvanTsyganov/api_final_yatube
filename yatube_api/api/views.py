from rest_framework import viewsets, permissions, filters, mixins
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
# local
from posts.models import Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    GroupSerializer, PostSerializer, CommentSerializer, FollowSerializer
)


class GetPostViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post_obj = get_object_or_404(Post, id=post_id)
        return post_obj.comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post_obj = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post_obj)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(GetPostViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['user__username', 'following__username']

    def get_queryset(self):
        queryset = self.request.user.follower
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
