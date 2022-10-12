from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS or
            request.user and request.user.is_staff)