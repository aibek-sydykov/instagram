from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from user.models import User
from user.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from user.permissions import IsUserOwnerOrReadOnly


class UserView(ModelViewSet):
    queryset = User.objects.prefetch_related('post_owner')
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = (IsUserOwnerOrReadOnly, )