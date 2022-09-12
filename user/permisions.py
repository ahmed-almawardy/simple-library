from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Allows access only to currnet user.
    """

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.id == obj.id)
