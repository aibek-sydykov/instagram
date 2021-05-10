from rest_framework import serializers
from user.models import User
from publication.serializers import PublicationsImagesSerializer
from publication.models import Publications


class PublicationsForUserSerializer(serializers.ModelSerializer):
    post_images = PublicationsImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Publications
        fields = ('id', 'text', 'date', 'post_images')


class UserSerializer(serializers.ModelSerializer):
    post_owner = PublicationsForUserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('phone', 'site', 'bio', 'avatar', 'username', 'first_name', 'last_name', 'email', 'post_owner')