from django.shortcuts import render, get_object_or_404
from rest_framework import status, request
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from topshiriq5.models import Post
from topshiriq5.permissions import  IsOwnerPermission
from topshiriq5.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerPermission,IsAuthenticated]
