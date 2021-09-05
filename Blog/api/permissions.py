from rest_framework.permissions import BasePermission
from rest_framework import permissions
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from .models import Post
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.owner



# content_type = ContentType.objects.get_for_model(Post)
# permission = Permission.objects.create(codename='can_hide',
#                                        name='can hide post',content_type=content_type)
