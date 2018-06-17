from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserListSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=150)

class UserSerializer(UserListSerializer):

    password = serializers.CharField()
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=254, required=False)

    def create(self, validated_data):
        user = User()
        return self.update(user, validated_data)


    def update(self, instance, validated_data):

        user = User()
        instance.set_password(validated_data.get('password'))
        instance.username = validated_data.get('username')
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.email = validated_data.get('email')
        instance.save()
        return instance

    def validate_username(self, username):
        if (self.instance is None or self.instance.username != username) and User.objects.filter(username=username).exists():
            raise ValidationError('Ya existe una cuenta con este username')

        return username
