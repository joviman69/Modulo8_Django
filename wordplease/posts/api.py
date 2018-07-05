from django.contrib.auth.models import User
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from blogs.models import Blog
from posts.models import Post
from posts.permissions import PostPermissions
from posts.serializers import PostListSerializer, PostDetailSerializer, NewPostSerializer

class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    permission_classes = [PostPermissions]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'intro', 'text']
    ordering_fields = ['creation_date']

    def get_serializer_class(self):
        if self.action == 'create':
            return NewPostSerializer
        elif self.action == 'list':
            return PostListSerializer
        else:
            return PostDetailSerializer

    def perform_create(self, serializer):
        userid = User.objects.get(username=self.request.user).id
        blogid = Blog.objects.get(owner=userid).id
        serializer.save(blog_id=blogid)

    def perform_update(self, serializer):
        userid = User.objects.get(username=self.request.user).id
        blogid = Blog.objects.get(owner=userid).id
        serializer.save(blog_id=blogid)
