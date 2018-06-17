from rest_framework.generics import ListAPIView

from blogs.models import Blog
from blogs.serializers import BlogListSerializer


class BlogListAPI(ListAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer

