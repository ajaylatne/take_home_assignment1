from rest_framework.permissions import BasePermission


class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user making the request is the owner of the object
        print(obj.author, request.user)
        return obj.author == request.user or request.user.is_superuser
