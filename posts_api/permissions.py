from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import User

class IsAuthorOrReadOnly(BasePermission):
    """
    Custom permission to only allow author of a post to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True
        
        id = request.user.token['user_id']
        user = User.objects.get(id=id)
        
        # Write permissions are only allowed to the owner of the snippet.
        return obj.author == user