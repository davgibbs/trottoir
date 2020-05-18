from rest_framework import permissions


class CanAccessUserAdmin(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        # Instance must have an attribute named `user`.
        return request.user.access_user_admin