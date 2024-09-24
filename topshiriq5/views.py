from django.shortcuts import get_object_or_404, render
from rest_framework import request, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from topshiriq5.models import Post, Product, ProductSerializer
from topshiriq5.permissions import IsOwnerPermission
from topshiriq5.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerPermission, IsAuthenticated]
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
