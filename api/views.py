from rest_framework import viewsets, filters
from django_filters import rest_framework as dgango_filtres

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import get_object_or_404

from .serializers import PostSerializer, CommentSerializer, GroupSerializer, \
    FollowSerializer
from .models import Post, Comment, Group, Follow
from .permissions import IsOwnerOrReadOnly, CantFollowOnUrSelf


class PostViewSetApi(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [dgango_filtres.DjangoFilterBackend]
    filterset_fields = ['group', ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSetApi(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        queryset = self.get_queryset()
        serializer.save(author=self.request.user, post_id=post_id)

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, pk=post_id)
        queryset = Comment.objects.select_related('post').filter(post=post)
        return queryset


class GroupViewSetApi(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ('post', 'get')
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class FlowViewSetApi(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = [filters.SearchFilter]
    http_method_names = ('post', 'get')
    search_fields = ['=user__username', '=following__username']
    permission_classes = [IsAuthenticatedOrReadOnly, CantFollowOnUrSelf]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
