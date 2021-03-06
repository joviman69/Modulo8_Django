from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostListSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = ['id', 'title', 'image', 'intro', 'publication_date']


class NewPostSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = ['title', 'intro', 'text', 'image', 'creation_date', 'publication_date', 'type']


class PostDetailSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = '__all__'
