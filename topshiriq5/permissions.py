from rest_framework import permissions

from topshiriq5.models import Post
from topshiriq5.serializers import PostSerializer


class IsOwnerPermission(permissions.BasePermission):
    """
    Faqat post egasi yangilash yoki o'chirish mumkin.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
