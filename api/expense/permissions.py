from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


# Without use for now
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        raise PermissionDenied()
