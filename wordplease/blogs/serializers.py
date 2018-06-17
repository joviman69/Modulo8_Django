from rest_framework.serializers import ModelSerializer

from blogs.models import Blog


class BlogListSerializer(ModelSerializer):

    class Meta:

        model = Blog
        fields = ['id', 'name']
